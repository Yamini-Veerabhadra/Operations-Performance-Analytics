# Power BI reproduction kit

Generate analysis-ready CSV files:

```bash
python -m scripts.build_reports
```

In Power BI Desktop select **Get Data > Text/CSV** for:
- `data/processed/monthly_performance.csv`
- `data/processed/state_performance.csv`
- `data/processed/daily_metrics.csv`
- `data/processed/data_quality.csv`

Suggested pages:
1. Executive Performance: orders, delivery success, eligible deliveries, late rate.
2. Monthly Trends: monthly orders, late rate, date slicer.
3. Regional Operations: order count vs late rate, state slicer.
4. AI & Quality: anomaly flags and quality audit table.

Example DAX (in relevant tables):
```
Total Orders = SUM(monthly_performance[orders])
Eligible Deliveries = SUM(monthly_performance[eligible])
Late Deliveries = SUM(monthly_performance[late])
Late Rate % = DIVIDE([Late Deliveries], [Eligible Deliveries], 0) * 100
```

**No `.pbix` is included.** The reports and documented DAX are a reproducible build kit; Power BI Desktop is required to create an actual `.pbix` file.
