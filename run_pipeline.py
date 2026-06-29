import subprocess
import time

def run_step(name, command):
    print(f"\n🚀 Running {name}...")
    start = time.time()

    result = subprocess.run(command, shell=True)

    end = time.time()

    if result.returncode != 0:
        print(f"❌ {name} FAILED")
        exit(1)

    print(f"✅ {name} completed in {round(end - start, 2)} sec")


print("===================================")
print(" SMART CITY DATA PIPELINE STARTING ")
print("===================================")

run_step("Bronze Layer", "python3 src/bronze/bronze_ingestion.py")
run_step("Silver Layer", "python3 src/silver/silver_cleaning.py")
run_step("Gold Layer", "python3 src/gold/gold_aggregations.py")

print("\n🎉 PIPELINE SUCCESSFULLY COMPLETED")