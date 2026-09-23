{{ config(materialized='view') }}

SELECT
    * EXCLUDE (
        "order_date",
        "shipping_date"
    ),

    "order_date" AS order_datetime,

    "shipping_date" AS shipping_datetime

FROM {{ source('supply_chain', 'SUPPLY_CHAIN_RAW') }}