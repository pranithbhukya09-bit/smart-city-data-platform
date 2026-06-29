import streamlit as st
from pyspark.sql import SparkSession

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Smart City Dashboard", layout="wide")

st.title("🚕 Smart City Data Platform Dashboard")

# ---------------- SPARK SESSION ----------------
spark = SparkSession.builder.appName("Dashboard").getOrCreate()

# Load data
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
gold_path = BASE_DIR / "datasets" / "processed" / "gold" / "revenue_by_location"

df = spark.read.parquet(str(gold_path))

# KEEP ONLY REQUIRED COLUMNS
df = df.select("pickup_location", "total_revenue")

pdf = df.toPandas()

# Optional rename for dashboard clarity
pdf.columns = ["location", "revenue"]

# ---------------- KPI SECTION ----------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

# Total records
col1.metric("Total Records", len(pdf))

# Top revenue location (SAFE: based on max revenue)
top_row = pdf.loc[pdf["revenue"].idxmax()]
col2.metric("Top Revenue Location", top_row["location"])

# Max revenue
max_revenue = pdf["revenue"].max()
col3.metric("Max Revenue", round(float(max_revenue), 2))

# ---------------- DATA TABLE ----------------
st.subheader("📍 Revenue by Location")
st.dataframe(pdf.sort_values("revenue", ascending=False))

# ---------------- CHART ----------------
st.subheader("📈 Revenue Distribution")
st.bar_chart(pdf.set_index("location")["revenue"])