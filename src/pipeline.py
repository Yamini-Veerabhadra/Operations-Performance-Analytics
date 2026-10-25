"""Reproducible Olist data loading, joins, quality audit, and reporting exports."""
from pathlib import Path
import pandas as pd
import numpy as np

RAW_NAMES = {
 'orders':'olist_orders_dataset.csv', 'customers':'olist_customers_dataset.csv',
 'items':'olist_order_items_dataset.csv','payments':'olist_order_payments_dataset.csv',
 'products':'olist_products_dataset.csv','sellers':'olist_sellers_dataset.csv',
 'reviews':'olist_order_reviews_dataset.csv','geolocation':'olist_geolocation_dataset.csv',
 'categories':'product_category_name_translation.csv'}
DATES=['order_purchase_timestamp','order_approved_at','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date']

def load_tables(folder, include_all=False):
    folder=Path(folder)
    required=['orders','customers','items','payments']
    names=list(RAW_NAMES) if include_all else required
    tables={}
    for key in names:
        p=folder/RAW_NAMES[key]
        if not p.exists():
            if key in required: raise FileNotFoundError(f'Required dataset missing: {p}')
            continue
        tables[key]=pd.read_csv(p,low_memory=False)
    for field in DATES:
        tables['orders'][field]=pd.to_datetime(tables['orders'][field], errors='coerce')
    return tables

def quality_report(tables):
    o=tables['orders']; c=tables['customers']; i=tables['items'];p=tables['payments']
    checks={
      'Duplicate order IDs':int(o.order_id.duplicated().sum()),
      'Null order IDs':int(o.order_id.isna().sum()),
      'Missing purchase timestamps':int(o.order_purchase_timestamp.isna().sum()),
      'Delivered orders missing delivery timestamps':int((o.order_status.eq('delivered')&o.order_delivered_customer_date.isna()).sum()),
      'Carrier handover missing for delivered orders':int((o.order_status.eq('delivered')&o.order_delivered_carrier_date.isna()).sum()),
      'Delivery timestamp before carrier handover':int((o.order_delivered_customer_date<o.order_delivered_carrier_date).fillna(False).sum()),
      'Orders without a customer match':int((~o.customer_id.isin(c.customer_id)).sum()),
      'Item rows without an order match':int((~i.order_id.isin(o.order_id)).sum()),
      'Payment rows without an order match':int((~p.order_id.isin(o.order_id)).sum()),
    }
    return pd.DataFrame([{'check':k,'flagged_rows':v} for k,v in checks.items()])

def order_facts(tables):
    o=tables['orders'].copy();c=tables['customers'];i=tables['items'];p=tables['payments']
    # Aggregate one-to-many data BEFORE joining to avoid item x payment row multiplication.
    items=i.groupby('order_id',as_index=False).agg(item_count=('order_item_id','count'),items_value=('price','sum'),freight_value=('freight_value','sum'),seller_count=('seller_id','nunique'))
    payment=p.groupby('order_id',as_index=False).agg(payment_total=('payment_value','sum'),payment_records=('payment_sequential','count'))
    o=o.merge(c[['customer_id','customer_state','customer_city']],on='customer_id',how='left',validate='many_to_one')
    o=o.merge(items,on='order_id',how='left',validate='one_to_one').merge(payment,on='order_id',how='left',validate='one_to_one')
    o['eligible']=o.order_status.eq('delivered') & o.order_delivered_customer_date.notna() & o.order_estimated_delivery_date.notna()
    o['late']=o.eligible & (o.order_delivered_customer_date>o.order_estimated_delivery_date)
    o['on_time']=o.eligible & ~o.late
    seconds=(o.order_delivered_customer_date-o.order_delivered_carrier_date).dt.total_seconds()/86400
    o['shipping_days']=seconds.where(seconds>=0)
    o['purchase_month']=o.order_purchase_timestamp.dt.to_period('M').astype(str)
    return o

def by_dimension(facts,dimension='customer_state',minimum=30):
    if dimension not in ['customer_state','purchase_month','order_status']:
        raise ValueError('Unsupported dimension')
    t=facts.groupby(dimension,dropna=False).agg(orders=('order_id','nunique'),delivered=('order_status',lambda s:int(s.eq('delivered').sum())),eligible=('eligible','sum'),late=('late','sum'),on_time=('on_time','sum'),revenue=('payment_total','sum'),avg_transit_days=('shipping_days','mean')).reset_index()
    t['late_rate']=np.where(t.eligible.gt(0),t.late/t.eligible*100,np.nan)
    t['on_time_rate']=np.where(t.eligible.gt(0),t.on_time/t.eligible*100,np.nan)
    return t.loc[t.orders>=minimum].sort_values('orders',ascending=False)

def root_cause_slice(facts, month='2018-03', state='RJ'):
    subset=facts[facts.purchase_month.eq(month)&facts.customer_state.eq(state)&facts.eligible].copy()
    subset['approval_to_carrier_days']=(subset.order_delivered_carrier_date-subset.order_approved_at).dt.total_seconds()/86400
    return subset.groupby('late').agg(orders=('order_id','count'),avg_shipping_days=('shipping_days','mean'),avg_approval_to_carrier_days=('approval_to_carrier_days','mean')).reset_index()

def export_reports(tables, destination):
    from src.analytics import daily_metrics,detect_anomalies
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    facts=order_facts(tables); daily=daily_metrics(tables['orders']); anomalies=detect_anomalies(daily)
    outputs={'daily_metrics':daily,'anomaly_analysis':anomalies,'data_quality':quality_report(tables),'state_performance':by_dimension(facts,'customer_state',0),'monthly_performance':by_dimension(facts,'purchase_month',0),'march_2018_rj_investigation':root_cause_slice(facts)}
    for label,frame in outputs.items():frame.to_csv(destination/f'{label}.csv',index=False)
    return outputs
