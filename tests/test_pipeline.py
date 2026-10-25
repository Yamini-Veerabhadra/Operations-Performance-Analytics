import pandas as pd
from src.pipeline import load_tables,quality_report,order_facts,by_dimension,root_cause_slice
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_real_data_pipeline():
    tables=load_tables(ROOT/'data'/'raw')
    facts=order_facts(tables)
    assert len(facts)==99441
    assert facts.order_id.nunique()==99441
    assert int(facts.order_status.eq('delivered').sum())==96478
    assert int(facts.eligible.sum())==96470
    assert int(facts.late.sum())==7826
    checks=quality_report(tables).set_index('check').flagged_rows
    assert checks['Delivered orders missing delivery timestamps']==8
    assert checks['Carrier handover missing for delivered orders']==2
    assert checks['Delivery timestamp before carrier handover']==23
    states=by_dimension(facts,'customer_state',minimum=100)
    assert 'RJ' in states.customer_state.values
    investigation=root_cause_slice(facts,'2018-03','RJ')
    assert investigation.orders.sum()==864
    assert investigation.loc[investigation.late,'orders'].iloc[0]==319
