from src.utils.data_quality import (
    validate_schema,
    validate_nulls,
    validate_duplicates,
    validate_row_count
)
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, hour, dayofweek

# -------------------------
# Spark Session
# -------------------------
spark = SparkSession.builder \
    .appName("ChicagoTaxiSilverLayer") \
    .getOrCreate()

# -------------------------
# Paths
# -------------------------
from src.config.config import SILVER_INPUT, SILVER_OUTPUT

INPUT_PATH = SILVER_INPUT
OUTPUT_PATH = SILVER_OUTPUT
# -------------------------
# Read Bronze data
# -------------------------
df = spark.read.parquet(INPUT_PATH)
expected_columns = [
    "trip_id",
    "pickup_datetime",
    "dropoff_datetime",
    "trip_seconds",
    "trip_miles",
    "pickup_location",
    "dropoff_location",
    "fare",
    "tip",
    "payment_type"
]

validate_schema(df, expected_columns)
validate_row_count(df)
validate_nulls(df, ["fare", "trip_miles", "trip_seconds"])
validate_duplicates(df, ["trip_id"])
# -------------------------
# Type Casting
# -------------------------
df = df.withColumn("trip_seconds", col("trip_seconds").cast("int")) \
       .withColumn("trip_miles", col("trip_miles").cast("float")) \
       .withColumn("fare", col("fare").cast("float")) \
       .withColumn("tip", col("tip").cast("float"))

# -------------------------
# Feature Engineering
# -------------------------
df = df.withColumn("trip_duration_minutes", col("trip_seconds") / 60) \
       .withColumn("total_revenue", col("fare") + col("tip")) \
       .withColumn("revenue_per_mile", col("total_revenue") / col("trip_miles"))

df = df.withColumn("pickup_datetime", to_timestamp("pickup_datetime")) \
       .withColumn("hour_of_day", hour("pickup_datetime")) \
       .withColumn("day_of_week", dayofweek("pickup_datetime"))

# -------------------------
# Clean Data
# -------------------------
df = df.dropna()

# -------------------------
# Write Silver Layer
# -------------------------
df.write.mode("overwrite").parquet(OUTPUT_PATH)

print("Silver layer completed successfully!")
