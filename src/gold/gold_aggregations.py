from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count, desc

spark = SparkSession.builder \
    .appName("ChicagoTaxiGoldLayer") \
    .getOrCreate()
from src.config.config import GOLD_INPUT, GOLD_OUTPUT

INPUT_PATH = GOLD_INPUT
OUTPUT_PATH = GOLD_OUTPUT
df = spark.read.parquet(INPUT_PATH)

# -------------------------
# 1. Revenue by Location
# -------------------------
revenue_by_location = df.groupBy("pickup_location") \
    .agg(
        sum("total_revenue").alias("total_revenue"),
        count("*").alias("total_trips"),
        avg("trip_miles").alias("avg_distance")
    ) \
    .orderBy(desc("total_revenue"))

# -------------------------
# 2. Peak Hour Analysis
# -------------------------
peak_hours = df.groupBy("hour_of_day") \
    .agg(
        count("*").alias("trip_count"),
        avg("total_revenue").alias("avg_revenue")
    ) \
    .orderBy(desc("trip_count"))

# -------------------------
# 3. Payment Type Distribution
# -------------------------
payment_distribution = df.groupBy("payment_type") \
    .agg(count("*").alias("count"))

# -------------------------
# Save Gold Layer
# -------------------------
revenue_by_location.write.mode("overwrite").parquet(f"{OUTPUT_PATH}/revenue_by_location")
peak_hours.write.mode("overwrite").parquet(f"{OUTPUT_PATH}/peak_hours")
payment_distribution.write.mode("overwrite").parquet(f"{OUTPUT_PATH}/payment_distribution")

print("Gold layer completed successfully!")
