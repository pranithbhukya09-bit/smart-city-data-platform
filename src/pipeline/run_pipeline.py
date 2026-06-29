import subprocess
import sys
import time
from src.utils.logger import get_logger

logger = get_logger("PIPELINE")

PYTHON = sys.executable  # ensures same python environment

def run_step(name, module_path):
    logger.info(f"Starting {name}")

    start = time.time()

    result = subprocess.run(
        [PYTHON, "-m", module_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        logger.error(result.stderr)
        logger.error(f"{name} FAILED")
        exit(1)

    end = time.time()

    logger.info(f"{name} completed in {round(end - start, 2)} sec")


logger.info("SMART CITY DATA PIPELINE STARTED")

run_step("Bronze Layer", "src.bronze.bronze_ingestion")
run_step("Silver Layer", "src.silver.silver_cleaning")
run_step("Gold Layer", "src.gold.gold_aggregations")

logger.info("PIPELINE COMPLETED SUCCESSFULLY")
