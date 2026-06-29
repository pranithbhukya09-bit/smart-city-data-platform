from pyspark.sql import DataFrame

# ---------------------------
# Schema Validation (STRICT)
# ---------------------------
def validate_schema(df: DataFrame, expected_columns: list):
    missing = set(expected_columns) - set(df.columns)

    if missing:
        raise Exception(f"SCHEMA ERROR: Missing columns -> {missing}")

    print("✅ Schema validation passed")


# ---------------------------
# Null Validation (FAIL FAST)
# ---------------------------
def validate_nulls(df: DataFrame, columns: list, max_null_ratio=0.0):
    total_rows = df.count()

    for col in columns:
        nulls = df.filter(df[col].isNull()).count()
        ratio = nulls / total_rows

        if ratio > max_null_ratio:
            raise Exception(f"NULL ERROR: {col} has {ratio:.2%} nulls")

        print(f"✅ {col}: null ratio {ratio:.2%}")


# ---------------------------
# Duplicate Validation (STRICT)
# ---------------------------
def validate_duplicates(df: DataFrame, subset_columns: list):
    total = df.count()
    distinct = df.dropDuplicates(subset_columns).count()

    dup = total - distinct

    if dup > 0:
        raise Exception(f"DUPLICATE ERROR: {dup} duplicate rows found")

    print("✅ No duplicates found")


# ---------------------------
# Row Count Safety Check
# ---------------------------
def validate_row_count(df: DataFrame, min_rows=1):
    count = df.count()

    if count < min_rows:
        raise Exception(f"ROW ERROR: Only {count} rows found")

    print(f"✅ Row count OK: {count}")
