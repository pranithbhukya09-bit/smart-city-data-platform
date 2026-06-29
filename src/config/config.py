# =========================
# Smart City Data Pipeline Config
# =========================

BASE_PATH = "datasets"

# Bronze Layer
BRONZE_INPUT = f"{BASE_PATH}/raw/taxi_trips.csv"
BRONZE_OUTPUT = f"{BASE_PATH}/processed/bronze"

# Silver Layer
SILVER_INPUT = f"{BASE_PATH}/processed/bronze"
SILVER_OUTPUT = f"{BASE_PATH}/processed/silver"

# Gold Layer
GOLD_INPUT = f"{BASE_PATH}/processed/silver"
GOLD_OUTPUT = f"{BASE_PATH}/processed/gold"
