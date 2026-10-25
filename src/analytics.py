"""Order-level operational metrics, data checks and anomaly detection."""
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

REQUIRED = {"order_id", "customer_id", "order_status", "order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"}


def read_orders(path_or_buffer):
    df = pd.read_csv(path_or_buffer, low_memory=False)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Required columns missing: {', '.join(sorted(missing))}")
    for c in ["order_purchase_timestamp", "order_delivered_customer_date", "order_estimated_delivery_date"]:
        df[c] = pd.to_datetime(df[c], errors="coerce")
    return df


def validate_orders(df):
    return pd.DataFrame([
        {"check": "Duplicate order_id rows", "count": int(df.order_id.duplicated().sum())},
        {"check": "Missing order IDs", "count": int(df.order_id.isna().sum())},
        {"check": "Missing purchase timestamp", "count": int(df.order_purchase_timestamp.isna().sum())},
        {"check": "Delivered orders missing delivery date", "count": int(((df.order_status == "delivered") & df.order_delivered_customer_date.isna()).sum())},
        {"check": "Delivery before purchase", "count": int((df.order_delivered_customer_date < df.order_purchase_timestamp).fillna(False).sum())},
    ])


def daily_metrics(df):
    d = df.dropna(subset=["order_purchase_timestamp"]).copy()
    d["day"] = d.order_purchase_timestamp.dt.floor("D")
    d["delivered"] = d.order_status.eq("delivered")
    # Only delivered orders with both dates qualify for on-time delivery rate.
    d["delivery_eligible"] = d.delivered & d.order_delivered_customer_date.notna() & d.order_estimated_delivery_date.notna()
    d["on_time"] = d.delivery_eligible & (d.order_delivered_customer_date <= d.order_estimated_delivery_date)
    d["late"] = d.delivery_eligible & ~d.on_time
    out = d.groupby("day", as_index=False).agg(orders=("order_id", "nunique"), delivered=("delivered", "sum"), eligible=("delivery_eligible", "sum"), on_time=("on_time", "sum"), late=("late", "sum"))
    out["on_time_rate"] = np.where(out.eligible.gt(0), out.on_time / out.eligible * 100, np.nan)
    out["late_rate"] = np.where(out.eligible.gt(0), out.late / out.eligible * 100, np.nan)
    return out.sort_values("day")


def detect_anomalies(metrics, contamination=0.05):
    result = metrics.copy()
    # Daily order volume is observable at purchase time; historical delivery outcomes
    # are descriptive and not used as if they were contemporaneously available.
    if len(result) < 20:
        result["anomaly"] = False
        result["anomaly_score"] = np.nan
        return result
    result["weekday"] = result.day.dt.dayofweek
    result["rolling_orders"] = result.orders.shift(1).rolling(14, min_periods=7).median()
    result["volume_change"] = (result.orders - result.rolling_orders) / result.rolling_orders.replace(0, np.nan)
    valid = result.volume_change.notna() & np.isfinite(result.volume_change)
    result["anomaly"] = False
    result["anomaly_score"] = np.nan
    if valid.sum() >= 20:
        features = result.loc[valid, ["orders", "weekday", "volume_change"]].to_numpy(dtype=float)
        model = IsolationForest(n_estimators=150, contamination=contamination, random_state=42)
        result.loc[valid, "anomaly"] = model.fit_predict(features) == -1
        result.loc[valid, "anomaly_score"] = model.decision_function(features)
    return result
