# Supply Chain Data Engineering Pipeline

Built an end-to-end pipeline using PySpark, Snowflake, and dbt to process supply chain order data into analytics-ready tables.

## Architecture

```
Raw CSV
   |
   v
PySpark (cleaning, QA checks, dimension + fact tables)
   |
   v
Parquet
   |
   v
Snowflake
   |
   v
dbt Staging
   |
   v
dbt Mart
   |
   v
Data Quality Tests
```

## Tech Stack

Python, PySpark, Snowflake, dbt, Parquet, Snowflake Python Connector

## Dataset

Raw dataset: 180,519 order-item records across 53 columns.

After cleaning:
- 180,519 order-item records
- 65,752 orders
- 20,652 customers
- 118 products
- 46 cleaned columns

Raw CSV is included under `data/raw/`.

## PySpark

Cleans and standardizes the raw data, then builds customer, product, and date dimension tables plus an order-item fact table. Processed data is written to Parquet.

## Snowflake

Processed Parquet files are loaded in via the Snowflake Python Connector — stages the files, infers schema, loads the data, and validates the row count.

## dbt

`stg_supply_chain` — staging layer
`fct_order_performance` — mart layer with order-level metrics: total sales, profit, discount, item count, avg shipping days, scheduled shipping days, late delivery risk

## Data Quality

PySpark checks: nulls, duplicate IDs, customer/category ID consistency, fact-table key integrity
dbt tests: not_null, unique

Latest run: 6/6 dbt tests passed, 0 errors, 0 warnings, 180,519 records processed.

## Key Skills Demonstrated

Distributed data processing, ETL design, dimensional modeling, cloud data warehousing, SQL transformations, data quality/validation, pipeline orchestration

## Running It

```bash
git clone https://github.com/sanjay-s22/supply-chain-data-pipeline.git
cd supply-chain-data-pipeline
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Set Snowflake env vars:

```bash
export SNOWFLAKE_ACCOUNT="your-account"
export SNOWFLAKE_USER="your-user"
export SNOWFLAKE_PRIVATE_KEY_PATH="/path/to/rsa_key.p8"
```

Then run:

```bash
python run_pipeline.py
```

Runs PySpark ETL -> Snowflake Load -> dbt Build + Tests

---

**Note:** keep your actual Snowflake account, username, key path, and any credentials out of this file — placeholders only.