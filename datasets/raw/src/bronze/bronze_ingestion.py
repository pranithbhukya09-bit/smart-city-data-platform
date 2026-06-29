from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
import os

# -------------------------
# Spark Session
# -------------------------
spark = SparkSession.builder \
    .appName("ChicagoTaxiBronzeLayer") \
    .getOrCreate()

# -------------------------
# Input Path
# -------------------------
BASE_PATH = "datasets/raw"
INPUT_FILE = os.path.join(BASE_PATH, "taxi_trips.csv")

# -------------------------
# Read CSV
# -------------------------
df = spark.read.option("header", True).csv(INPUT_FILE)

print("Initial Schema:")
df.printSchema()

print("Row Count:", df.count())

# -------------------------
# Add ingestion metadata
# -------------------------
df = df.withColumn("ingestion_timestamp", current_timestamp())

# -------------------------
# Write Bronze Layer (Parquet)
# -------------------------
OUTPUT_PATH = "datasets/processed/bronze"

df.write.mode("overwrite").parquet(OUTPUT_PATH)

print("Bronze layer written successfully!")
