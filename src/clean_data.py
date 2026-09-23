from pyspark.sql.functions import to_timestamp


def clean_data(df):

    # Remove sensitive columns
    df = df.drop(
        "Customer Password",
        "Customer Email",
        "Customer Fname",
        "Customer Lname",
        "Customer Street",
        "Product Description",
        "Product Image"
    )

    # Rename columns
    rename_map = {
        "Type": "order_type",
        "Days for shipping (real)": "actual_shipping_days",
        "Days for shipment (scheduled)": "scheduled_shipping_days",
        "Benefit per order": "benefit_per_order",
        "Sales per customer": "sales_per_customer",
        "Delivery Status": "delivery_status",
        "Late_delivery_risk": "late_delivery_risk",
        "Category Id": "category_id",
        "Category Name": "category_name",
        "Customer City": "customer_city",
        "Customer Country": "customer_country",
        "Customer Id": "customer_id",
        "Customer Segment": "customer_segment",
        "Customer State": "customer_state",
        "Customer Zipcode": "customer_zipcode",
        "Department Id": "department_id",
        "Department Name": "department_name",
        "Latitude": "latitude",
        "Longitude": "longitude",
        "Market": "market",
        "Order City": "order_city",
        "Order Country": "order_country",
        "Order Customer Id": "order_customer_id",
        "order date (DateOrders)": "order_date",
        "Order Id": "order_id",
        "Order Item Cardprod Id": "order_item_cardprod_id",
        "Order Item Discount": "order_item_discount",
        "Order Item Discount Rate": "order_item_discount_rate",
        "Order Item Id": "order_item_id",
        "Order Item Product Price": "order_item_product_price",
        "Order Item Profit Ratio": "order_item_profit_ratio",
        "Order Item Quantity": "order_item_quantity",
        "Sales": "sales",
        "Order Item Total": "order_item_total",
        "Order Profit Per Order": "order_profit_per_order",
        "Order Region": "order_region",
        "Order State": "order_state",
        "Order Status": "order_status",
        "Order Zipcode": "order_zipcode",
        "Product Card Id": "product_card_id",
        "Product Category Id": "product_category_id",
        "Product Name": "product_name",
        "Product Price": "product_price",
        "Product Status": "product_status",
        "shipping date (DateOrders)": "shipping_date",
        "Shipping Mode": "shipping_mode"
    }

    for old_name, new_name in rename_map.items():
        df = df.withColumnRenamed(old_name, new_name)

    # Convert dates
    df = (
        df
        .withColumn(
            "order_date",
            to_timestamp("order_date", "M/d/yyyy H:mm")
        )
        .withColumn(
            "shipping_date",
            to_timestamp("shipping_date", "M/d/yyyy H:mm")
        )
    )

    return df