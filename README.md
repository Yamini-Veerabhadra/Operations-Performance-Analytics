
# Operations Performance & Anomaly Detection

### End-to-End Data Analytics | SQL | Python | Machine Learning | Business Intelligence

An end-to-end operations analytics project designed to monitor business performance, investigate delivery delays, identify unusual order-volume patterns, and improve data-driven decision-making.

The project combines **Python, PostgreSQL, SQL, Scikit-learn, Streamlit, and Power BI reporting resources** to demonstrate an analytics workflow from raw data to business insights.

The application uses the **Olist Brazilian E-Commerce Dataset**, containing approximately 100,000 historical orders from 2016–2018.

> **Note:** This is a portfolio demonstration using historical data, not a live logistics monitoring system.

---

## 1. Project Overview

Businesses handling large order volumes need reliable reporting to identify operational issues and performance trends.

This project addresses questions such as:

- How many orders are successfully delivered?
- What percentage of deliveries arrive on time?
- Which regions experience higher delivery delays?
- Are there unusual changes in daily order volumes?
- Which operational stages are associated with longer delays?
- Are missing or inconsistent records affecting reporting accuracy?

The application provides interactive dashboards, automated data-quality checks, machine learning-based anomaly screening, and downloadable analytical reports.

---

## 2. Key Features

### Executive Overview
- Total orders and delivered orders
- Delivery success and on-time delivery rates
- Order-volume trends
- Operational performance summaries

### Operations & Regional Analytics
- Delivery performance by customer location
- Regional comparisons
- Shipping duration analysis
- Identification of high-delay regions

### AI Anomaly Monitoring
- Isolation Forest-based anomaly detection
- Identification of unusual daily order-volume patterns
- Interactive anomaly visualizations
- Adjustable anomaly detection sensitivity

### Investigation Dashboard
- Monthly and regional drill-down analysis
- Late versus on-time delivery comparisons
- Shipping duration investigation
- Identification of potential contributing factors

### Data Quality Monitoring
- Missing-value detection
- Duplicate record checks
- Negative shipping-duration checks
- Referential integrity validation
- Data-quality reporting

### Reports & Methodology
- Downloadable KPI reports
- Anomaly analysis exports
- Metric definitions
- Analytical methodology and limitations

---

## 3. Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database | PostgreSQL |
| Querying | SQL |
| Machine Learning | Scikit-learn, Isolation Forest |
| Web Application | Streamlit |
| Visualization | Plotly |
| Business Intelligence | Power BI reporting kit, DAX |
| Testing | Pytest |
| Version Control | Git, GitHub |
| Deployment Target | Streamlit Community Cloud |

---

## 4. Dataset

**Source:** Olist Brazilian E-Commerce Public Dataset

Dataset link:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains approximately 100,000 orders and includes:

- Customer information
- Order status and timestamps
- Order items
- Payment records
- Seller information
- Product information
- Customer reviews
- Geographic information

All nine original CSV files are preserved in `data/raw/`.

The application primarily uses orders, customers, order items, and payments for its analytical workflow.

Dataset attribution and redistribution conditions should be reviewed before publishing the raw files.

---

## 5. Data Processing Workflow

The project follows this workflow:

1. Load historical source data.
2. Validate missing, duplicate, and inconsistent records.
3. Clean and transform data using Pandas.
4. Aggregate order items and payments before joining to order-level records.
5. Calculate operational KPIs.
6. Perform exploratory and regional analysis.
7. Apply anomaly detection.
8. Generate interactive dashboards and reports.
9. Validate calculations through automated tests.

**Data Flow:**

```text
Olist CSV Datasets
        |
        v
Python / Pandas ETL
        |
        v
Data Validation & Reconciliation
        |
        v
Analytical Datasets
        |
        +----> SQL / PostgreSQL
        |
        +----> Operational KPI Analysis
        |
        +----> AI Anomaly Detection
        |
        v
Streamlit Dashboard
        |
        +----> Interactive Analysis
        +----> CSV Reports
        +----> Power BI Reporting Data
```

---

## 6. Key Performance Indicators

| Metric | Definition |
|---|---|
| Total Orders | Number of unique orders |
| Delivered Orders | Orders with delivered status |
| Delivery Success Rate | Delivered orders / Total orders × 100 |
| On-Time Delivery Rate | On-time deliveries / Delivered orders with valid delivery and estimated dates × 100 |
| Late Delivery Rate | Late deliveries / Eligible delivered orders × 100 |
| Transit Time | Customer delivery timestamp − Carrier handover timestamp |
| Long Shipping Rate | Share of valid deliveries with transit time exceeding the selected threshold |

The long-shipping threshold is an exploratory analytical rule, not an official delivery service-level agreement.

---

## 7. Selected Analytical Findings

The historical dataset analysis produced the following results:

| Metric | Result |
|---|---:|
| Total Orders | 99,441 |
| Delivered Orders | 96,478 |
| Delivery Success Rate | 97.02% |
| On-Time Delivery Rate | 91.89% |
| Delivered Orders with Valid Delivery Dates | 96,470 |
| On-Time Deliveries | 88,644 |
| Late Deliveries | 7,826 |

### March 2018 Delivery Investigation

March 2018 had a late delivery rate of **21.36%** among eligible delivered orders purchased that month.

In Rio de Janeiro (RJ):

- Delivered orders: 864
- Late deliveries: 319
- Late delivery rate: 36.92%
- Average transit time for late deliveries: 35.38 days
- Average transit time for on-time deliveries: 12.71 days

These findings suggest that longer carrier-to-customer transit times were associated with delivery delays.

**These observations do not establish the underlying cause of the delays.**

---

## 8. Machine Learning Approach

The project uses **Isolation Forest**, an unsupervised anomaly detection algorithm.

### Purpose

Identify unusual patterns in daily historical order volumes.

### Approach

1. Aggregate historical orders by day.
2. Prepare features for anomaly screening.
3. Apply Isolation Forest.
4. Generate anomaly scores and flags.
5. Visualize unusual patterns.
6. Support analyst investigation of flagged periods.

### Limitations

- Flagged anomalies are not automatically verified business incidents.
- The model does not establish causation.
- Dataset coverage gaps can influence anomaly detection.
- No supervised anomaly-classification accuracy is claimed.
- The application does not make validated future forecasts.

---

## 9. Run the Project Locally

### Prerequisites

- Python 3.11 or later with compatible dependencies
- Visual Studio Code or another code editor
- Git
- PostgreSQL (optional)

### Step 1 — Open the Project Folder

Open the directory containing:

```text
app.py
requirements.txt
src/
scripts/
data/
tests/
```

### Step 2 — Create Virtual Environment

```powershell
python -m venv .venv
```

### Step 3 — Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the following command for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment again.

### Step 4 — Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 5 — Run Automated Tests

```powershell
python -m pytest -q
```

Verified local test result:

```text
2 passed
```

### Step 6 — Launch the Application

```powershell
python -m streamlit run app.py
```

Open:

http://localhost:8501

The application loads its bundled historical data automatically.

---

## 10. Generate Reporting Data

Run:

```powershell
python -m scripts.build_reports
```

Generated reporting files are saved in:

```text
data/processed/
```

These outputs can be used for additional analysis and Power BI reporting.

---

## 11. PostgreSQL Integration

PostgreSQL integration is available as an optional analytical workflow.

Create a dedicated database named:

```text
operations_analytics
```

Configure the connection using a local environment variable:

```powershell
$env:DATABASE_URL="postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/operations_analytics"
```

Run the database loader:

```powershell
python -m scripts.load_postgres
```

The loader imports the source datasets into PostgreSQL tables.

**Important:** The loader replaces its target tables when executed. Use it only with a dedicated project database. Do not run it against databases containing unrelated data.

SQL reporting scripts are available in:

```text
sql/02_business_reporting.sql
```

Credentials must never be committed to GitHub.

---

## 12. Power BI Reporting

The project includes a Power BI reporting kit containing:

- Prepared analytical datasets
- KPI definitions
- DAX measure examples
- Suggested dashboard structure
- Reporting instructions

Suggested report pages:

1. Operations Overview
2. Delivery Performance
3. Regional Analysis
4. Anomaly & Data Quality Analysis

**Note:** A completed Power BI `.pbix` file is not included in the current repository. The included resources support building the report in Power BI Desktop.

---

## 13. Deployment

The Streamlit application is structured for deployment through Streamlit Community Cloud.

### Deployment Process

1. Push the repository to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Create a new application from the GitHub repository.
4. Select `app.py` as the entry point.
5. Configure application settings and dependencies.
6. Deploy and verify the hosted application.

The application reads CSV files from `data/raw/`.

Deployment resource limits and dataset redistribution conditions should be checked before publishing.

**Current deployment status:** Locally tested. Public cloud deployment has not yet been completed.

---

## 14. Project Structure

```text
Operations-Performance-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
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
│   └── 02_business_reporting.sql
│
├── data/
│   ├── raw/
│   ├── reference/
│   └── processed/
│
├── powerbi/
│   └── README.md
│
└── tests/
    ├── test_analytics.py
    └── test_pipeline.py
```

---

## 15. Testing & Validation

The project includes automated tests covering core analytical functionality and data processing.

Testing areas include:

- Order-level aggregation
- Data transformation
- KPI calculations
- Data-quality validation
- Anomaly detection output
- Analytical pipeline functionality

**Verified result:** 2 automated tests passed during local execution.

The tests provide initial validation but do not constitute exhaustive production testing.

---

## 16. Skills Demonstrated

This project demonstrates:

- SQL querying and relational data analysis
- Python-based data processing
- ETL pipeline development
- Data cleaning and validation
- Exploratory data analysis
- KPI reporting
- Business intelligence
- Machine learning integration
- Operational anomaly investigation
- Data visualization
- Automated testing
- Technical documentation
- Web application development

---

## 17. Project Limitations

- Historical data, not a real-time feed
- No verified carrier-level root-cause attribution
- No production deployment claimed
- No measured cost savings or operational improvements claimed
- Anomaly detection is exploratory
- The Power BI report must be built separately from the provided reporting kit

---

## 18. Future Improvements

- Deploy the application publicly
- Add PostgreSQL-backed dashboard queries
- Complete the Power BI report
- Expand operational anomaly detection to additional KPIs
- Add statistical comparisons and investigation summaries
- Improve dashboard usability and responsive design
- Expand automated test coverage

---

## Data Attribution

Dataset: **Olist Brazilian E-Commerce Public Dataset**

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The project is developed for portfolio, learning, and demonstration purposes.


## Live Application

**[Launch Operations Intelligence Dashboard](https://operations-performance-analytics.streamlit.app/)**

Explore operational KPIs, delivery performance, regional analytics, AI anomaly detection, data-quality monitoring, and interactive investigations.