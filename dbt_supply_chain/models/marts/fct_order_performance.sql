{{ config(materialized='table') }}

SELECT
    "order_id" AS order_id,
    "order_customer_id" AS customer_id,

    CAST(order_datetime AS DATE) AS order_date,

    "market" AS market,
    "order_region" AS order_region,
    "order_country" AS order_country,
    "order_state" AS order_state,
    "order_status" AS order_status,
    "shipping_mode" AS shipping_mode,

    COUNT(DISTINCT "order_item_id") AS order_item_count,

    SUM("order_item_quantity") AS total_quantity,

    SUM("sales") AS total_sales,

    SUM("order_item_discount") AS total_discount,

    MAX("order_profit_per_order") AS total_profit,

    AVG("actual_shipping_days") AS avg_shipping_days,

    MAX("scheduled_shipping_days") AS scheduled_shipping_days,

    MAX("late_delivery_risk") AS late_delivery_risk

FROM {{ ref('stg_supply_chain') }}

GROUP BY
    "order_id",
    "order_customer_id",
    order_datetime,
    "market",
    "order_region",
    "order_country",
    "order_state",
    "order_status",
    "shipping_mode"