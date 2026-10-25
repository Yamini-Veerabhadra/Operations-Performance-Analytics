"""Optional PostgreSQL loader. Needs DATABASE_URL in environment; no passwords in Git."""
import os
from pathlib import Path
from sqlalchemy import create_engine, text
from src.pipeline import RAW_NAMES
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]

def main():
    url=os.environ.get('DATABASE_URL')
    if not url:raise SystemExit('Set DATABASE_URL before importing, e.g. postgresql+psycopg://user:password@localhost:5432/operations_analytics')
    engine=create_engine(url,pool_pre_ping=True)
    with engine.connect() as con:con.execute(text('SELECT 1'))
    for name,file in RAW_NAMES.items():
        p=ROOT/'data'/'raw'/file
        if not p.exists():continue
        rows=0
        for frame in pd.read_csv(p,chunksize=20000,low_memory=False):
            for col in frame.columns:
                if col.endswith('_timestamp') or col in ['order_approved_at','order_delivered_carrier_date','order_delivered_customer_date','order_estimated_delivery_date','shipping_limit_date','review_creation_date','review_answer_timestamp']:
                    frame[col]=pd.to_datetime(frame[col],errors='coerce')
            frame.to_sql('olist_'+name,engine,schema='public',if_exists='replace' if rows==0 else 'append',index=False,chunksize=2000,method='multi')
            rows+=len(frame)
        print(f'olist_{name}: {rows:,} records')
    print('Import finished. Run sql/02_business_reporting.sql in pgAdmin for reporting views.')
if __name__=='__main__':main()
