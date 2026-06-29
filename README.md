# 🚀 Smart City Data Platform (Medallion Architecture with PySpark)

A scalable end-to-end **data engineering pipeline** built using **PySpark, medallion architecture, and modular ETL design principles**.  
The project processes raw urban mobility (Chicago Taxi-like) data into analytics-ready datasets.

---

## 📌 Project Overview

This project simulates a real-world smart city data system using a layered architecture:

- Bronze Layer → Raw data ingestion
- Silver Layer → Data cleaning & transformation
- Gold Layer → Aggregated analytics

Designed for scalability and cloud migration (Azure Databricks / AWS EMR).

---

## 🏗️ Architecture

Raw Data (CSV)
      ↓
Bronze Layer (PySpark Ingestion)
      ↓
Silver Layer (Data Cleaning)
      ↓
Gold Layer (Aggregations)
      ↓
Parquet Outputs for Analytics

---

## ⚙️ Tech Stack

### Core Data Engineering
- PySpark 3.5+
- Spark SQL
- Distributed Data Processing

### Programming
- Python 3
- SQL

### Data Formats
- CSV
- Parquet

### Architecture Concepts
- Medallion Architecture (Bronze / Silver / Gold)
- Modular ETL Design
- Scalable Data Pipelines

### DevOps
- Git & GitHub
- CI/CD (GitHub Actions)

---

## 📊 Features

- End-to-end ETL pipeline (Bronze → Gold)
- Modular PySpark architecture
- Data cleaning & type casting
- Scalable distributed processing design
- Analytics outputs:
  - Revenue by location
  - Peak hour analysis
  - Payment distribution trends

---

## 📁 Project Structure

smart-city-data-platform/

datasets/
  raw/
  processed/
    bronze/
    silver/
    gold/

src/
  bronze/
  silver/
  gold/
  config/
  pipeline/
  utils/

adf/
dashboard/
notebooks/
sql/
tests/

run_pipeline.py
requirements.txt
README.md

---

## 🚀 How to Run This Project Locally

### 📌 Prerequisites

Make sure you have the following installed:

- Python 3.9+
- pip
- Java (JDK 8 or 11 recommended for PySpark)
- PySpark installed (`pyspark==3.5.1` recommended)

---

### ⚙️ 1. Clone the Repository

```bash
git clone git@github.com:pranithbhukya09-bit/smart-city-data-platform.git
cd smart-city-data-platform

📦 2. Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate
📥 3. Install Dependencies
pip install -r requirements.txt
🗂️ 4. Verify Dataset Exists

Make sure your raw dataset is placed here:

datasets/raw/taxi_trips.csv

If not, add your CSV file there before running.

🚀 5. Run Full Pipeline

Run the complete Medallion ETL pipeline:

python3 -m src.pipeline.run_pipeline
📊 6. Expected Output

After successful execution, you will see:

Bronze layer processed (raw ingestion)
Silver layer cleaned data
Gold layer aggregated analytics

Output files will be generated in:

datasets/processed/
  ├── bronze/
  ├── silver/
  └── gold/
🧪 7. (Optional) Run Individual Layers
Bronze Layer
python3 src/bronze/bronze_ingestion.py
Silver Layer
python3 src/silver/silver_cleaning.py
Gold Layer
python3 src/gold/gold_aggregations.py