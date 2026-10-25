"""Operations Intelligence: historical Olist operational analytics demo."""
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from src.analytics import daily_metrics,detect_anomalies
from src.pipeline import load_tables,order_facts,quality_report,by_dimension,root_cause_slice

ROOT=Path(__file__).resolve().parent
st.set_page_config(page_title='Operations Intelligence',page_icon='📦',layout='wide')
st.title('Operations Intelligence')
st.caption('AI-assisted operational performance & data quality | Olist historical e-commerce orders, 2016–2018')

@st.cache_data(show_spinner='Loading historical order datasets…')
def cached_tables():return load_tables(ROOT/'data'/'raw')

with st.sidebar:
    st.header('Analysis settings')
    st.caption('All data is historical. Do not interpret this as a live operational feed.')
    contamination=st.slider('AI anomaly fraction (exploratory)',0.01,0.15,0.05,0.01)
    st.divider()
    st.markdown('**Dataset:** [Olist Brazilian E-Commerce](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)')
    st.caption('Models flag patterns for human investigation, not confirmed business incidents.')

try:
    tables=cached_tables()
except (FileNotFoundError,ValueError) as e:
    st.error(str(e));st.info('Place the four required Olist CSV files in data/raw/ as described in README.md.');st.stop()

facts=order_facts(tables)
daily=daily_metrics(tables['orders'])
flags=detect_anomalies(daily,contamination=contamination)
quality=quality_report(tables)
state=by_dimension(facts,'customer_state',minimum=100)
monthly=by_dimension(facts,'purchase_month',minimum=100)

p1,p2,p3,p4,p5,p6=st.tabs(['Executive overview','Operations & regions','AI anomaly monitoring','Investigation','Data quality','Reports & methodology'])
with p1:
    a,b,c,d=st.columns(4)
    n=len(facts);eligible=int(facts.eligible.sum());late=int(facts.late.sum())
    a.metric('Orders',f'{n:,}');b.metric('Delivered',f"{int(facts.order_status.eq('delivered').sum()):,}")
    c.metric('On-time deliveries',f'{(1-late/eligible)*100:.2f}%' if eligible else 'N/A')
    d.metric('Flagged days',f'{int(flags.anomaly.sum()):,}')
    st.plotly_chart(px.line(daily,x='day',y='orders',title='Daily orders by purchase date'),use_container_width=True)
    st.plotly_chart(px.line(monthly.sort_values('purchase_month'),x='purchase_month',y='late_rate',markers=True,title='Late-delivery rate by purchase month (%)'),use_container_width=True)
    st.info('Delivery outcomes are based on eventual order status, grouped by purchase date. Do not use them for real-time same-day decisions.')
with p2:
    st.subheader('Regional performance')
    states=state.sort_values('late_rate',ascending=False)
    st.plotly_chart(px.bar(states,x='customer_state',y='late_rate',hover_data=['eligible','late','orders'],title='Late-delivery rate by customer state (minimum 100 orders)'),use_container_width=True)
    st.dataframe(states.rename(columns={'customer_state':'state'}),use_container_width=True,hide_index=True)
    st.subheader('Monthly operational trends')
    st.dataframe(monthly.sort_values('purchase_month'),use_container_width=True,hide_index=True)
with p3:
    st.subheader('Daily volume anomaly screening')
    st.write('Isolation Forest uses daily order counts, weekday and change vs. preceding 14 recorded days. This is exploratory **in-sample** detection; contamination is user-selected and is not a validated alert precision.')
    flagged=flags.copy();flagged['class']=np.where(flagged.anomaly,'Flagged','Regular')
    st.plotly_chart(px.scatter(flagged,x='day',y='orders',color='class',hover_data=['volume_change','anomaly_score'],title='Unusual daily order-volume patterns'),use_container_width=True)
    st.dataframe(flagged[flagged.anomaly][['day','orders','volume_change','anomaly_score']].sort_values('anomaly_score'),use_container_width=True,hide_index=True)
    st.warning('Dataset start/end periods may contain incomplete date coverage. A flagged day is not a confirmed incident or causal diagnosis.')
with p4:
    st.subheader('Investigate month and state')
    valid_months=sorted(facts.purchase_month.dropna().unique())
    month=st.selectbox('Purchase month',valid_months,index=valid_months.index('2018-03') if '2018-03' in valid_months else len(valid_months)-1)
    states_list=sorted(facts.customer_state.dropna().unique())
    customer_state=st.selectbox('Customer state',states_list,index=states_list.index('RJ') if 'RJ' in states_list else 0)
    cases=facts[facts.purchase_month.eq(month)&facts.customer_state.eq(customer_state)&facts.eligible]
    c1,c2,c3=st.columns(3)
    c1.metric('Eligible deliveries',f'{len(cases):,}')
    c2.metric('Late deliveries',f'{int(cases.late.sum()):,}')
    c3.metric('Late rate',f'{cases.late.mean()*100:.2f}%' if len(cases) else 'N/A')
    if len(cases):
        compare=root_cause_slice(facts,month,customer_state)
        st.dataframe(compare,use_container_width=True,hide_index=True)
        st.plotly_chart(px.bar(compare,x='late',y='avg_shipping_days',color='late',title='Mean carrier-to-customer transit days: on-time vs late'),use_container_width=True)
    st.caption('Group comparisons identify associations, not proven causes. Exclude invalid transit durations from shipping averages; group counts may include records with missing transit timestamps.')
with p5:
    st.subheader('Quality & reconciliation audit')
    st.dataframe(quality,use_container_width=True,hide_index=True)
    st.write('Raw values are preserved; invalid durations become null in analysis. No silent row deletions or fake data corrections.')
    st.metric('Total flagged validation instances',f"{int(quality.flagged_rows.sum()):,}")
    st.caption('Counts across checks can overlap. This sum is not the number of unique affected orders.')
with p6:
    st.subheader('Export analysis-ready reports')
    reports={'Daily KPI reporting':daily,'Anomaly screening':flags,'Regional KPIs':state,'Monthly KPIs':monthly,'Data quality audit':quality}
    for label,df in reports.items():
        st.download_button(f'Download {label}',df.to_csv(index=False).encode('utf-8'),file_name=label.lower().replace(' ','_')+'.csv',mime='text/csv',key=label)
    st.markdown('''**Metric definitions**
- **Delivered**: order status equals `delivered` (not an on-time measure).
- **Eligible**: delivered orders with actual and estimated delivery timestamps.
- **On-time / late**: actual delivery timestamp <= / > estimated delivery timestamp, respectively.
- **Transit days**: actual customer delivery − carrier handover, excluding missing/negative spans.
- **Order/payment grain**: item and payment rows aggregated to order level before joins to prevent multiplication.
- **AI flags**: unsupervised exploratory screening only; lower Isolation Forest score is more anomalous.

**Data ethics:** Public historical e-commerce data, not current operational telemetry. No proof of root cause, fraud, carrier identity, or production ML accuracy. ''')
