# E-Commerce Sales Data Pipeline & Dashboard

An end-to-end data engineering project that extracts, validates, transforms, stores, analyzes, and visualizes e-commerce sales data using Python, SQLite, SQL, and Streamlit.

## Project Overview
This project demonstrates a complete data pipeline for e-commerce sales data.

This pipeline:
1. Extracts data from a CSV file
2. Validates the data
3. Transforms the data
4. Loads the data into a SQLite database
5. Uses SQL to analyze the data
6. Displays business insights through an interactive Streamlit dashboard

Technologies used in this project
Python for pipeline and data processing
Pandas/NumPy for data transformation
SQLite/SQL fordatabase and analysis
Streamlit for dashboard
Git/GitHub for version control and portfolio

## Pipeline Architecture
CSV Dataset
     |
Extract
     |
Validate
     |
Transform
     |
Load into SQLite Database
     |
SQL Analysis
     |
Streamlit Dashboard


Data Validation & Transformation
The pipeline performs several data quality checks before loading the data into the database.

 Validation:
- Checks for missing values
- Checks for duplicate records
- Validates quantities
- Validates product prices
- Validates discount percentages
- Validates shipping costs
- Validates total sales values

Transformations
The pipeline creates additional business-related fields, including:
- Year
- Month
- Month Name
- Profit Margin
- Profit Status
- Sales Per Unit
- High Value Order

## Database & SQL Analysis
The transformed data is stored in a SQLite database.
SQL queries are used to answer business questions such as:
- What are the top products by revenue?
- What are the most profitable products?
- Which customer segments generate the most revenue?
- Which products have the highest number of units sold?
- How does revenue change by year?
- Which customer segments generate the most profit?
- How many orders are high-value orders?


## Dashboard
The Streamlit dashboard provides an interactive view of the e-commerce data.
### Dashboard Features
- Total Orders KPI
- Total Revenue KPI
- Total Profit KPI
- Total Units Sold KPI
- Top 10 Products by Revenue
- Top 10 Products by Profit
- Revenue by Year
- High-Value vs Normal Orders
- Year-based filtering

## Project Results
The pipeline successfully processed 2,000 e-commerce orders.

Key results from the dataset:
- Total Orders: 2,000
- Total Revenue: 484,559.34
- Total Profit: 158,872.32
- Total Units Sold: 7,115
The dashboard allows these results to be filtered by year.

## Project Structure
E-Commerce-Sales-Pipeline/
 app.py                    # Streamlit dashboard
 pipeline.py               # Data extraction, validation, transformation and loading
 global_ecommerce_sales.csv # Source dataset
 Sales_Pipeline.db         # SQLite database
 requirements.txt          # Python dependencies
 README.md                 # Project documentation


 ## How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd E-Commerce-Sales-Pipeline
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Run the data pipeline

```bash
python pipeline.py
```

This extracts the CSV data, validates it, transforms it, and loads it into the SQLite database.

### 4. Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

The dashboard will then open in your web browser.
