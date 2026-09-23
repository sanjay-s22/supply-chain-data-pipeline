from pyspark.sql.functions import monotonically_increasing_id 
from pyspark.sql.functions import (to_date, year, month, dayofmonth, dayofweek, quarter, date_format)



def create_dim_customer(df):
    dim_customer = (
        df.select(
            'customer_id',
            'customer_segment',
            'customer_city',
            'customer_state',
            'customer_country',
            'customer_zipcode'
        ).dropDuplicates(['customer_id'])
    )

    #surrogate key
    dim_customer = dim_customer.withColumn(
        'customer_key',
        monotonically_increasing_id()
    )

    return dim_customer


def create_dim_product(df):
    dim_product = (
        df.select(
            'product_card_id',
            'product_name',
            'product_price',
            'product_status',
            'category_id',
            'category_name',
            'department_id',
            'department_name'
        ).dropDuplicates(['product_card_id'])
    )

    dim_product = dim_product.withColumn(
        'product_key',
        monotonically_increasing_id()
    )
    
    return dim_product 


def create_dim_date(df):
    dim_date= (
        df.select(
            to_date('order_date').alias('date')
        ).distinct()
        .withColumn('year', year('date'))
        .withColumn('month', month('date'))
        .withColumn('day', dayofmonth('date'))
        .withColumn('day_of_week', dayofweek('date'))
        .withColumn('quarter', quarter('date'))
        .withColumn(
            "date_key",
            date_format("date", "yyyyMMdd").cast("int")
        )
    )

    
    return dim_date


def create_fact_order_items(
    df,
    dim_customer,
    dim_product,
    dim_date
):

    fact = (
        df
        .join(
            dim_customer.select(
                "customer_id",
                "customer_key"
            ),
            on="customer_id",
            how="left"
        )
        .join(
            dim_product.select(
                "product_card_id",
                "product_key"
            ),
            on="product_card_id",
            how="left"
        )
        .withColumn(
            "date_key",
            date_format("order_date", "yyyyMMdd").cast("int")
        )
        .select(
            "order_item_id",
            "order_id",

            "customer_key",
            "product_key",
            "date_key",

            "order_item_quantity",
            "order_item_product_price",
            "order_item_discount",
            "order_item_discount_rate",
            "order_item_total",
            "sales",
            "benefit_per_order",
            "order_profit_per_order",
            "order_item_profit_ratio",

            "shipping_mode",
            "actual_shipping_days",
            "scheduled_shipping_days",
            "delivery_status",
            "late_delivery_risk",
            "order_status"
        )
    )

    return fact
