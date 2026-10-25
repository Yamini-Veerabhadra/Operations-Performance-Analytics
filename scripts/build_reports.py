"""Run with: python -m scripts.build_reports"""
from pathlib import Path
from src.pipeline import load_tables,export_reports
ROOT=Path(__file__).resolve().parents[1]
if __name__=='__main__':
    reports=export_reports(load_tables(ROOT/'data'/'raw'),ROOT/'data'/'processed')
    for k,v in reports.items():print(f'{k}: {len(v):,} rows')
