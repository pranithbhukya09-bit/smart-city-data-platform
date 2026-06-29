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

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt