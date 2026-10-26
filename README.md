# Operations Performance & Anomaly Detection

**End-to-End Data Analytics | SQL | Python | Machine Learning | Power BI | Streamlit**

An end-to-end, AI-enabled operations analytics project designed to monitor business performance, analyze delivery efficiency, identify unusual order-volume patterns, investigate operational bottlenecks, and support data-driven business decisions.

The project combines **Python, Pandas, PostgreSQL, SQL, Scikit-learn, Streamlit, Plotly, and Power BI** to demonstrate a complete analytics workflow, from raw data processing and validation to machine learning, interactive dashboards, and business reporting.

Built using the **Olist Brazilian E-Commerce Dataset**, containing 99,441 historical orders from 2016–2018.

### Live Application

**[Launch Operations Intelligence Dashboard](https://operations-performance-analytics.streamlit.app/)**

**[GitHub Repository](https://github.com/Yamini-Veerabhadra/Operations-Performance-Analytics)**

> **Note:** This is a portfolio and educational demonstration using historical e-commerce data. The application is publicly deployed but does not connect to live logistics systems or monitor real-time business transactions.

---

## 1. Project Overview

Organizations handling large volumes of orders need accurate operational reporting to monitor fulfillment performance, investigate delivery delays, and identify areas requiring attention.

Traditional reporting may show performance changes without providing sufficient context to understand contributing factors.

This project combines business intelligence, exploratory analytics, automated data validation, and unsupervised machine learning to support operational performance investigation.

### Business Questions

- How many orders are successfully delivered?
- What percentage of deliveries arrive before or on the estimated delivery date?
- Which months experience unusually high delivery delays?
- Which customer locations have higher late-delivery rates?
- How do shipping durations differ between late and on-time orders?
- Are unusual changes occurring in daily order volumes?
- Are missing, duplicate, or inconsistent records affecting reporting accuracy?
- How can analysts communicate operational findings through interactive dashboards?

### Project Objectives

1. Develop a reproducible analytical data pipeline.
2. Calculate and validate operational KPIs.
3. Identify delivery performance trends and regional differences.
4. Apply AI-based anomaly detection to historical order-volume patterns.
5. Investigate potential contributing factors behind operational performance changes.
6. Develop interactive Streamlit and Power BI dashboards.
7. Provide downloadable reports and clearly documented analytical findings.

---

## 2. Project Deliverables

The repository contains:

- A publicly deployed six-tab Streamlit application.
- A four-page Power BI report in editable `.pbip` format.
- Python-based data cleaning and transformation pipelines.
- PostgreSQL integration scripts and SQL reporting queries.
- An Isolation Forest anomaly-detection implementation.
- Data-quality validation and reconciliation logic.
- Prepared reporting datasets and CSV exports.
- Automated tests using Pytest.
- Power BI dashboard screenshots.
- Project documentation and reproducible setup instructions.

---

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Database | PostgreSQL |
| Data Querying | SQL |
| Machine Learning | Scikit-learn, Isolation Forest |
| Interactive Application | Streamlit |
| Data Visualization | Plotly |
| Business Intelligence | Microsoft Power BI, DAX |
| Testing | Pytest |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

---

## 4. Dataset

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Source:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains approximately 100,000 historical orders and multiple related tables.

### Source Files

| Dataset | Description |
|---|---|
| `olist_orders_dataset.csv` | Order status and purchase/delivery timestamps |
| `olist_customers_dataset.csv` | Customer identifiers and geographic information |
| `olist_order_items_dataset.csv` | Ordered products, sellers, and item-level values |
| `olist_order_payments_dataset.csv` | Payment transactions and payment methods |
| `olist_order_reviews_dataset.csv` | Customer review information |
| `olist_products_dataset.csv` | Product attributes and categories |
| `olist_sellers_dataset.csv` | Seller identifiers and locations |
| `olist_geolocation_dataset.csv` | Geographic reference data |
| `product_category_name_translation.csv` | Product category translations |

The original nine CSV files are maintained in `data/raw/`.

The primary application workflow uses orders, customers, order items, and payments, while the additional source files support extended analysis.

**Data handling:** Public historical data is used for demonstration. Dataset attribution, redistribution conditions, and repository size limits should be reviewed when publishing or redistributing raw files.

---

## 5. End-to-End Data Workflow

The analytical workflow consists of the following stages:

1. **Data Ingestion:** Load historical CSV datasets.
2. **Data Validation:** Identify null values, duplicate records, invalid timestamps, and unmatched references.
3. **Data Transformation:** Clean records and prepare analysis-ready datasets.
4. **Data Modeling:** Combine related datasets while preserving order-level accuracy.
5. **KPI Calculation:** Compute order, delivery, shipping, and regional performance metrics.
6. **Exploratory Analysis:** Investigate trends, geographic differences, and operational exceptions.
7. **AI Anomaly Detection:** Identify unusual daily order-volume patterns using Isolation Forest.
8. **Business Intelligence:** Present findings through Streamlit and Power BI.
9. **Reporting:** Generate downloadable analytical datasets.
10. **Testing:** Validate calculations and data-processing functionality.

### Data Flow

```text
Olist Historical CSV Datasets
              |
              v
       Python / Pandas
              |
              v
    Data Cleaning & Validation
              |
              v
     Analytical Data Modeling
              |
      +-------+--------+
      |                |
      v                v
 PostgreSQL        KPI Calculations
 & SQL Queries          |
      |                 v
      |           Anomaly Detection
      |                 |
      +--------+--------+
               |
               v
       Reporting Datasets
               |
       +-------+--------+
       |                |
       v                v
 Streamlit Dashboard  Power BI Report
       |                |
       v                v
Interactive Analysis  Business Reporting
```

### Order-Level Data Integrity

Order items and payment information are aggregated before being joined to order-level records.

This prevents duplicate joins from incorrectly inflating order counts, payment totals, and other analytical metrics.

Original source records are preserved separately from transformed datasets.

---

## 6. Streamlit Application

**Live Demo:** https://operations-performance-analytics.streamlit.app/

The Streamlit application provides six analytical modules.

### 6.1 Executive Overview

Provides a high-level view of operational performance.

Features include:

- Total order count
- Delivered order count
- Delivery success rate
- On-time delivery rate
- Daily and monthly order trends
- Operational performance summaries

### 6.2 Operations & Regions

Supports regional and operational performance analysis.

Features include:

- Customer state-level analysis
- Regional order-volume comparisons
- Late-delivery rate comparisons
- Shipping duration analysis
- Regional performance trends

### 6.3 AI Anomaly Monitoring

Uses unsupervised machine learning to identify unusual historical order-volume patterns.

Features include:

- Isolation Forest anomaly screening
- Anomaly scores
- Daily order-volume visualization
- Normal versus flagged-day comparisons
- Adjustable anomaly-detection sensitivity

### 6.4 Investigation

Supports deeper examination of unexpected operational performance.

Features include:

- Monthly performance investigation
- Regional drill-down
- Late versus on-time delivery comparisons
- Shipping-duration analysis
- Exploration of potential contributing factors

### 6.5 Data Quality

Provides visibility into source-data reliability.

Validation includes:

- Missing order identifiers
- Duplicate order records
- Missing timestamps
- Invalid shipping durations
- Negative transit-time records
- Unmatched data references

### 6.6 Reports & Methodology

Includes:

- Downloadable KPI reports
- Anomaly-analysis exports
- Metric definitions
- Analytical assumptions
- Data-quality methodology
- Interpretation limitations

---

## 7. Power BI Dashboard

The project includes an editable four-page Power BI dashboard for operational performance and business intelligence reporting.

**Power BI Project Location:** `Power Bi/Operations_Performance_Dashboard.pbip`

### Page 1 — Executive Overview

Provides management-level operational reporting.

Includes:

- Total Orders
- Delivered Orders
- Delivery Success Rate
- On-Time Delivery Rate
- Monthly Order Volume
- Monthly On-Time Delivery Rate
- Monthly Late Deliveries
- Monthly Operational Summary
- Purchase Month filtering

![Executive Overview](Screenshots/01_executive_overview.png)

### Page 2 — Delivery Performance

Focuses on delivery performance and transit-time analysis.

Includes:

- Delivery performance KPIs
- Monthly late-delivery trends
- Average transit duration
- On-time versus late-delivery comparisons
- Delivery performance reporting tables

![Delivery Performance](Screenshots/02_delivery_performance.png)

### Page 3 — Regional Operations

Analyzes operational performance across customer states.

Includes:

- State-level order volumes
- Regional delivery rates
- Average transit duration by state
- Regional performance comparisons
- State-level operational summaries

![Regional Operations](Screenshots/03_regional_operations.png)

### Page 4 — AI Anomalies & Data Quality

Combines anomaly-screening results and data-quality reporting.

Includes:

- AI-flagged anomaly days
- Anomaly scores over time
- Historical order-volume patterns
- Data-quality issue counts
- Anomaly investigation details

![AI Anomalies and Data Quality](Screenshots/04_ai_anomalies_data_quality.png)

### Opening the Power BI Report

1. Install Microsoft Power BI Desktop.
2. Open the repository's `Power Bi/` directory.
3. Open `Operations_Performance_Dashboard.pbip`.
4. Keep the associated `.Report` and `.SemanticModel` folders in the same directory.
5. If prompted, update local CSV data source paths and refresh the semantic model.

The report uses prepared analytical datasets generated from the Python pipeline.

**Note:** The Power BI dashboard is provided as an editable Power BI Project (`.pbip`), not a standalone `.pbix` file. Local data-source paths may need adjustment when opening the project on another computer.

---

## 8. Key Performance Indicators

| KPI | Definition |
|---|---|
| Total Orders | Count of unique orders |
| Delivered Orders | Orders with delivered status |
| Delivery Success Rate | Delivered orders divided by total orders |
| On-Time Delivery Rate | On-time orders divided by eligible delivered orders |
| Late Delivery Rate | Late deliveries divided by eligible delivered orders |
| Average Transit Days | Average carrier-to-customer shipping duration |
| Long Shipping Rate | Percentage of valid deliveries exceeding an exploratory shipping-duration threshold |
| AI Anomaly Days | Number of historical days flagged by the anomaly-screening model |

### Calculation Rules

- On-time delivery is determined by comparing the recorded customer delivery timestamp with the estimated delivery timestamp.
- Orders with missing required delivery timestamps are excluded from the applicable on-time delivery denominator.
- Negative transit durations are excluded from transit-time calculations.
- The original dataset is not modified when generating cleaned analytical views.
- Purchase-month analyses group orders by purchase date rather than the date when the final delivery outcome became available.

---

## 9. Selected Analytical Findings

The historical dataset produced the following operational results.

| Metric | Result |
|---|---:|
| Total Orders | 99,441 |
| Delivered Orders | 96,478 |
| Delivery Success Rate | 97.02% |
| Eligible Delivered Orders | 96,470 |
| On-Time Deliveries | 88,644 |
| Late Deliveries | 7,826 |
| On-Time Delivery Rate | 91.89% |
| Late Delivery Rate | 8.11% |

### Finding 1 — March 2018 Delivery Performance

March 2018 recorded:

- 7,003 eligible delivered orders
- 1,496 late deliveries
- 21.36% late-delivery rate

This was substantially higher than the overall historical late-delivery rate of 8.11%.

### Finding 2 — Rio de Janeiro Delivery Investigation

For Rio de Janeiro (RJ), March 2018:

| Metric | Result |
|---|---:|
| Delivered Orders | 864 |
| Late Deliveries | 319 |
| Late Delivery Rate | 36.92% |
| Average Transit Time — Late Orders | 35.38 days |
| Average Transit Time — On-Time Orders | 12.71 days |
| Average Approval-to-Carrier Time — Late Orders | 3.06 days |
| Average Approval-to-Carrier Time — On-Time Orders | 2.81 days |

Longer carrier-to-customer transit times were associated with late deliveries.

However, these findings do not prove which specific operational factor caused the delays.

### Finding 3 — Shipping Data Quality

Additional shipping-duration validation identified:

- 96,446 records in the cleaned shipping analysis view
- 23 delivered records with negative transit durations
- 2 delivered records with missing carrier timestamps
- 2,684 cleaned shipping records with transit durations exceeding 30 days
- 9.33 days average transit duration in the cleaned shipping view

The 30-day threshold is an exploratory analytical cutoff, not a documented contractual service-level agreement.

These findings demonstrate the importance of validating timestamp quality before reporting shipping performance.

---

## 10. Machine Learning — Anomaly Detection

### Algorithm

**Isolation Forest — Unsupervised Machine Learning**

Isolation Forest is used to screen historical daily order-volume patterns for unusual observations.

### Implementation

1. Aggregate orders at the daily level.
2. Prepare analytical features.
3. Fit the Isolation Forest model.
4. Calculate anomaly scores.
5. Flag observations classified as unusual.
6. Visualize results and support investigation.

### Business Application

The model helps analysts prioritize days that differ from typical historical order-volume patterns.

Potentially unusual periods can then be investigated using operational KPIs, regional breakdowns, and historical comparisons.

### Model Interpretation

Anomaly flags are investigative signals, not confirmed business incidents.

The number of flagged days depends on the model configuration, including its contamination setting.

The approach does not establish causation, automatically identify faulty carriers, or provide validated future forecasts.

No supervised classification accuracy or measured operational cost savings are claimed.

---

## 11. Data Quality & Validation

Data quality is an essential part of the analytical pipeline.

### Validation Areas

- Missing values
- Duplicate identifiers
- Date and timestamp consistency
- Negative transit durations
- Unmatched reference records
- Order-level aggregation accuracy
- Missing delivery information

### Validation Strategy

Source data is retained separately from cleaned analytical datasets.

Invalid records are documented and excluded only from calculations where they would make the resulting metric unreliable.

Different quality checks can identify overlapping records, so counts from separate checks should not automatically be added together as unique affected orders.

---

## 12. PostgreSQL & SQL Analytics

The project includes PostgreSQL integration and reusable SQL reporting logic.

SQL techniques demonstrated include:

- Joins
- Aggregations
- Filtering
- Common Table Expressions (CTEs)
- Window functions
- Conditional calculations
- SQL views
- KPI calculations
- Data-validation queries

### SQL Files

- `sql/01_order_kpis.sql`
- `sql/02_business_reporting.sql`

### PostgreSQL Integration

Create a dedicated PostgreSQL database:

```text
operations_analytics
```

Configure the database connection locally:

```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/operations_analytics"
```

Run the loader:

```powershell
python -m scripts.load_postgres
```

The loader imports the project datasets into PostgreSQL tables.

**Important:** The loader replaces its target tables when executed. Run it only against a dedicated project database.

Never commit passwords, private connection strings, or local secrets to GitHub.

PostgreSQL is an optional workflow; the deployed Streamlit demonstration loads its bundled CSV data without requiring a PostgreSQL connection.

---

## 13. Run the Project Locally

### Prerequisites

- Python 3.11 or later with compatible dependencies
- Git
- Visual Studio Code or another code editor
- PostgreSQL (optional)
- Power BI Desktop (for viewing/editing the Power BI project)

### Step 1 — Clone the Repository

```powershell
git clone https://github.com/Yamini-Veerabhadra/Operations-Performance-Analytics.git
```

Navigate to the project directory:

```powershell
cd Operations-Performance-Analytics
```

### Step 2 — Create a Virtual Environment

```powershell
python -m venv .venv
```

### Step 3 — Activate the Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 4 — Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 5 — Run Tests

```powershell
python -m pytest -q
```

Verified local test result:

```text
2 passed
```

### Step 6 — Launch the Streamlit Application

```powershell
python -m streamlit run app.py
```

Open the application locally:

http://localhost:8501

The application automatically loads the bundled historical datasets.

---

## 14. Generate Reporting Data

The project includes a reporting-data generation script.

Run:

```powershell
python -m scripts.build_reports
```

The generated reporting files are saved in:

```text
data/processed/
```

The reporting datasets include:

- Daily operational metrics
- Monthly performance
- Regional performance
- Anomaly analysis
- Data-quality reporting
- March 2018 Rio de Janeiro investigation

These files support reproducible analysis and Power BI reporting.

---

## 15. Project Structure

```text
Operations-Performance-Analytics/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── analytics.py
│   └── pipeline.py
│
├── scripts/
│   ├── build_reports.py
│   └── load_postgres.py
│
├── sql/
│   ├── 01_order_kpis.sql
│   └── 02_business_reporting.sql
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reference/
│
├── Power Bi/
│   ├── Operations_Performance_Dashboard.pbip
│   ├── Operations_Performance_Dashboard.Report/
│   ├── Operations_Performance_Dashboard.SemanticModel/
│   └── README.md
│
├── Screenshots/
│   ├── 01_executive_overview.png
│   ├── 02_delivery_performance.png
│   ├── 03_regional_operations.png
│   └── 04_ai_anomalies_data_quality.png
│
├── docs/
│   └── PROJECT_NOTES.md
│
└── tests/
    ├── test_analytics.py
    └── test_pipeline.py
```

**Note:** Local virtual environments, Python caches, temporary files, and credentials are not intended to be committed to GitHub.

---

## 16. Testing & Validation

Automated tests are implemented using Pytest.

The test suite covers aspects of:

- Analytical calculations
- Order aggregation
- Data transformation
- Data-quality checks
- Anomaly-detection outputs
- Multi-table analytical processing

### Verified Result

**2 automated tests passed during local execution.**

Testing provides initial verification of the analytical pipeline. The current suite is not intended to represent exhaustive production-level testing.

The Streamlit application has also been tested locally and deployed publicly.

---

## 17. Deployment

The Streamlit application is deployed using **Streamlit Community Cloud**.

### Live Dashboard

**https://operations-performance-analytics.streamlit.app/**

### Deployment Architecture

```text
GitHub Repository
       |
       v
Streamlit Community Cloud
       |
       v
Python Application
       |
       v
Bundled Historical Datasets
       |
       +----> KPI Analytics
       +----> Anomaly Detection
       +----> Regional Investigation
       +----> Data Quality Reporting
       |
       v
Public Interactive Dashboard
```

The application loads historical CSV data from the repository and runs the associated analytics components.

**Deployment Status:** Publicly deployed.

This deployment is a portfolio demonstration, not a production logistics system.

---

## 18. Skills Demonstrated

This project demonstrates hands-on application of:

### Data Analytics
- Exploratory Data Analysis
- Data Cleaning
- Data Validation
- KPI Development
- Trend Analysis
- Regional Analysis
- Operational Performance Investigation

### SQL & Databases
- PostgreSQL
- SQL Joins
- CTEs
- Window Functions
- Aggregations
- Analytical Views
- Data Reconciliation

### Python & Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Isolation Forest
- Automated Data Processing
- Unsupervised Anomaly Detection

### Business Intelligence
- Power BI
- DAX
- Interactive Dashboards
- KPI Reporting
- Operational Reporting
- Data Visualization
- Business Insights Communication

### Software & Deployment
- Streamlit
- Git
- GitHub
- Pytest
- Cloud Deployment
- Technical Documentation

---

## 19. Project Limitations

The project has the following limitations:

- Uses historical data instead of live operational feeds.
- Anomaly screening is exploratory rather than independently validated incident detection.
- Historical data coverage gaps can affect anomaly results.
- Does not establish causation for observed delivery delays.
- Does not identify specific carriers as responsible for delays.
- Does not claim measured operational savings.
- Uses a public Streamlit deployment for demonstration rather than a production logistics environment.
- Power BI may require local CSV data-source paths to be configured when opened on another computer.

These limitations are explicitly documented to support responsible interpretation of the results.

---

## 20. Future Improvements

Potential future improvements include:

- Connect PostgreSQL directly to the deployed analytical interface.
- Introduce scheduled data ingestion.
- Expand anomaly detection to additional operational KPIs.
- Compare Isolation Forest against statistical and seasonal baselines.
- Introduce stronger anomaly validation methods.
- Add statistical comparisons to investigation workflows.
- Expand automated test coverage.
- Improve accessibility and responsive dashboard design.
- Implement automated recurring management reports.

---

## 21. Data Attribution & Responsible Use

**Dataset:** Brazilian E-Commerce Public Dataset by Olist

**Source:** https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The project is intended for educational, analytical, and portfolio demonstration purposes.

All insights are derived from historical records and should not be interpreted as verified current business performance.

No private organizational credentials, confidential business records, or production system integrations are intended to be included in this public repository.

---

## 22. Project Summary

**Operations Performance & Anomaly Detection** demonstrates how SQL, Python, machine learning, and business intelligence can be combined to create a practical operational analytics solution.

The project covers the complete analytical workflow:

**Data Ingestion → Cleaning → Validation → Transformation → SQL Analysis → KPI Reporting → AI Anomaly Screening → Dashboard Visualization → Business Investigation**

By combining a publicly deployed Streamlit application with an editable Power BI report, the project demonstrates both interactive analytical application development and traditional business intelligence reporting.

The primary focus is delivering trustworthy metrics, investigating operational performance, and communicating data-driven findings clearly.