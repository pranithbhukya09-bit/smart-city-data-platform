from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
import os

spark = SparkSession.builder \
    .appName("ChicagoTaxiBronzeLayer") \
    .getOrCreate()

BASE_PATH = "datasets/raw"
from src.config.config import BRONZE_INPUT, BRONZE_OUTPUT

INPUT_FILE = BRONZE_INPUT
OUTPUT_PATH = BRONZE_OUTPUT
df = spark.read.option("header", True).csv(INPUT_FILE)

print("Schema:")
df.printSchema()

print("Row count:", df.count())

df = df.withColumn("ingestion_timestamp", current_timestamp())


df.write.mode("overwrite").parquet(OUTPUT_PATH)

print("Bronze layer completed")
