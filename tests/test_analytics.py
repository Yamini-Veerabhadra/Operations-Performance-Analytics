import pandas as pd
from src.analytics import daily_metrics, validate_orders, detect_anomalies


def test_metrics_delivery_eligibility():
    rows = pd.DataFrame({"order_id": ["1", "2"], "customer_id": ["a", "b"], "order_status": ["delivered", "canceled"], "order_purchase_timestamp": pd.to_datetime(["2018-01-01", "2018-01-01"]), "order_delivered_customer_date": pd.to_datetime(["2018-01-03", None]), "order_estimated_delivery_date": pd.to_datetime(["2018-01-04", None])})
    result = daily_metrics(rows)
    assert result.orders.iloc[0] == 2
    assert result.eligible.iloc[0] == 1
    assert result.on_time_rate.iloc[0] == 100
    assert validate_orders(rows).loc[3, 'count'] == 0
    assert not detect_anomalies(result).anomaly.any()
