# 🚕 Smart City Data Platform

A modern **Data Engineering project** that processes taxi trip data using **PySpark** and visualizes business insights through an interactive **Streamlit dashboard**.

The project demonstrates a complete **Bronze → Silver → Gold** data pipeline, following the Medallion Architecture used in production data platforms.

---

## 📌 Project Overview

The Smart City Data Platform ingests raw taxi trip data, transforms it into clean and aggregated datasets, and presents key business metrics such as:

- Revenue by pickup location
- Total trips by location
- Average trip distance
- Interactive dashboard with KPIs and charts

---

## 🏗️ Architecture

```
                Raw Taxi Data (CSV/Parquet)
                         │
                         ▼
                  Bronze Layer
               (Raw Ingested Data)
                         │
                         ▼
                  Silver Layer
          (Cleaned & Transformed Data)
                         │
                         ▼
                   Gold Layer
      (Business Aggregated Metrics)
                         │
                         ▼
              Streamlit Dashboard
```

---

## 📂 Project Structure

```
smart-city-data-platform/
│
├── dashboard/
│   └── app.py
│
├── datasets/
│   ├── raw/
│   └── processed/
│       ├── bronze/
│       ├── silver/
│       └── gold/
│
├── jobs/
│   ├── bronze_job.py
│   ├── silver_job.py
│   └── gold_job.py
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- PySpark
- Streamlit
- Pandas
- Apache Spark
- Parquet
- Git

---

## 📊 Dashboard Features

### KPIs
- Total Records
- Top Revenue Location
- Maximum Revenue

### Visualizations
- Revenue by Pickup Location
- Revenue Data Table
- Interactive Bar Chart

---

## 📁 Data Pipeline

### Bronze Layer
- Reads raw taxi trip dataset
- Stores raw data in Parquet format

### Silver Layer
- Cleans missing values
- Removes invalid records
- Standardizes data types

### Gold Layer
Generates business-ready datasets:

- Revenue by Pickup Location
- Total Trips by Pickup Location
- Average Trip Distance

---

## ▶️ Running the Project

### 1. Clone Repository

```bash
git clone <your-repository-url>
cd smart-city-data-platform
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run Data Pipeline

Bronze

```bash
python jobs/bronze_job.py
```

Silver

```bash
python jobs/silver_job.py
```

Gold

```bash
python jobs/gold_job.py
```

---

### 4. Launch Dashboard

```bash
cd dashboard
streamlit run app.py
```

---

## 📈 Example Gold Dataset

| Pickup Location | Total Revenue | Total Trips | Average Distance |
|-----------------|--------------:|------------:|-----------------:|
| Downtown | 128450.50 | 4210 | 4.8 |
| Airport | 98560.20 | 3120 | 8.5 |
| Midtown | 76420.75 | 2740 | 5.2 |

---

## 🎯 Learning Outcomes

This project demonstrates:

- Large-scale data processing with PySpark
- ETL pipeline development
- Medallion Architecture (Bronze, Silver, Gold)
- Data aggregation and analytics
- Interactive dashboard development
- Data engineering best practices

---

## 🚀 Future Enhancements

- Real-time streaming with Kafka
- Spark Structured Streaming
- Airflow pipeline orchestration
- Docker containerization
- AWS S3 data lake integration
- Delta Lake support
- Interactive map visualizations
- Time-series analytics
- Automated data quality checks

---

## 📸 Dashboard Preview

Dashboard includes:

- 📊 KPI cards
- 📈 Revenue distribution chart
- 📋 Revenue data table
- Business insights by pickup location