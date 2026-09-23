import os
import snowflake.connector


conn = snowflake.connector.connect(
    account=os.environ["SNOWFLAKE_ACCOUNT"],
    user=os.environ["SNOWFLAKE_USER"],
    private_key_file=os.environ["SNOWFLAKE_PRIVATE_KEY_PATH"],
    warehouse="COMPUTE_WH",
    database="SUPPLY_CHAIN_DW",
    schema="RAW",
    role="ACCOUNTADMIN",
)

cursor = conn.cursor()

try:
    print("Connected to Snowflake.")

    cursor.execute("""
        CREATE OR REPLACE FILE FORMAT SUPPLY_CHAIN_DW.RAW.PARQUET_FORMAT
        TYPE = PARQUET
    """)

    cursor.execute("""
        CREATE OR REPLACE TEMPORARY STAGE cleaned_data_stage
        FILE_FORMAT = SUPPLY_CHAIN_DW.RAW.PARQUET_FORMAT
    """)

    print("Uploading Parquet files...")

    cursor.execute("""
        PUT 'file:///home/sanjay/projects/supply-chain-pipeline/data/processed/cleaned_order_items/*.parquet'
        @cleaned_data_stage
        AUTO_COMPRESS = FALSE
        OVERWRITE = TRUE
    """)

    print("Upload complete.")

    cursor.execute("""
        CREATE OR REPLACE TABLE SUPPLY_CHAIN_DW.RAW.SUPPLY_CHAIN_RAW
        USING TEMPLATE (
            SELECT ARRAY_AGG(OBJECT_CONSTRUCT(*))
            FROM TABLE(
                INFER_SCHEMA(
                    LOCATION => '@cleaned_data_stage',
                    FILE_FORMAT => 'SUPPLY_CHAIN_DW.RAW.PARQUET_FORMAT'
                )
            )
        )
    """)

    cursor.execute("""
        COPY INTO SUPPLY_CHAIN_DW.RAW.SUPPLY_CHAIN_RAW
        FROM @cleaned_data_stage
        FILE_FORMAT = (FORMAT_NAME = 'SUPPLY_CHAIN_DW.RAW.PARQUET_FORMAT')
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
    """)

    cursor.execute("""
        SELECT COUNT(*)
        FROM SUPPLY_CHAIN_DW.RAW.SUPPLY_CHAIN_RAW
    """)

    count = cursor.fetchone()[0]

    print(f"Rows in RAW.SUPPLY_CHAIN_RAW: {count}")

finally:
    cursor.close()
    conn.close()