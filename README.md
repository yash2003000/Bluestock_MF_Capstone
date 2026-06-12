# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

The **Bluestock Mutual Fund Analytics Capstone Project** is an end-to-end financial analytics solution designed to analyze the Indian mutual fund industry using **Python, SQL, Power BI, and advanced risk analytics techniques**.

This project focuses on extracting meaningful insights from mutual fund datasets through **data cleaning, performance analysis, investor behaviour analytics, risk measurement, and dashboard development**. The objective is to build a structured analytical framework that supports informed investment decision-making through interactive visualizations and quantitative metrics.

---

## Project Objectives

The key objectives of this project are:

* Build an automated **ETL pipeline** for data ingestion, cleaning, and transformation.
* Create a structured **SQLite database** for efficient storage and querying.
* Perform **Exploratory Data Analysis (EDA)** to identify trends and patterns.
* Evaluate mutual fund performance using **financial performance metrics**.
* Conduct **advanced risk analysis** using VaR, CVaR, and rolling Sharpe Ratio.
* Analyze **investor behaviour and SIP continuity patterns**.
* Develop an **interactive Power BI dashboard** for business intelligence and decision-making.

---

## Tech Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* Matplotlib

### Database

* SQLite
* SQLAlchemy

### Visualization & Reporting

* Power BI
* Jupyter Notebook

### Version Control

* Git
* GitHub

---

## Project Structure

```text
bluestock_mf_capstone/
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_Advanced_Analytics.ipynb
├── scripts/
│   ├── data_ingestion.py
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── reports/
├── .gitignore
└── README.md
```

---

## Key Features

### 1. Mutual Fund Performance Analytics

* Sharpe Ratio
* Alpha & Beta Analysis
* Standard Deviation
* CAGR Analysis
* Maximum Drawdown

### 2. Advanced Risk Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Portfolio Concentration Analysis (HHI)

### 3. Investor Analytics

* Investor Cohort Analysis
* SIP Continuity Analysis
* At-Risk Investor Detection
* Transaction Behaviour Analysis

### 4. Fund Recommendation System

A simple rule-based recommendation engine suggests top mutual funds based on:

* Low Risk
* Moderate Risk
* High Risk

---

## Dashboard Pages

The interactive Power BI dashboard includes:

1. **Industry Overview** – AUM, SIP inflows, fund houses, and industry KPIs
2. **Fund Performance Analytics** – Risk vs Return, benchmark comparison, performance scorecards
3. **Investor Analytics** – Transaction patterns, demographics, investment behaviour
4. **SIP & Market Trends** – SIP inflows, category trends, and market comparison

---

## Key Deliverables

* ETL Pipeline Script
* SQLite Database
* Exploratory Data Analysis Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Report & Presentation

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-link>
cd bluestock_mf_capstone
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

### 4. Open Jupyter Notebooks

```bash
jupyter notebook
```

### 5. Open Dashboard

Open the Power BI dashboard file:

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

## Future Scope

* Live NAV API integration
* Portfolio optimization models
* Predictive analytics for fund performance
* Streamlit web application deployment

---

## Author

**Yash Chowdhary**
Bluestock Mutual Fund Analytics Capstone Project
