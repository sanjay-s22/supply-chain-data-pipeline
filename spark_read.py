from pyspark.sql import SparkSession 
from pyspark.sql.functions import to_timestamp
from pyspark.sql.functions import length


spark = (
    SparkSession.builder
    .appName('SupplyChainPipeline')
    .getOrCreate())

df = spark.read.csv('data/raw/Supplychaindataset.csv', header=True, inferSchema=True)

#print('Raw columns:', len(df.columns))

df = df.drop(
    'Customer Password',
    'Customer Fname',
    'Customer Lname',
    'Customer Email',
    'Customer Street',
    'Product Description',
    'Product Image'
)

df = (
    df
    .withColumnRenamed("Type", "order_type")
    .withColumnRenamed("Days for shipping (real)", "actual_shipping_days")
    .withColumnRenamed("Days for shipment (scheduled)", "scheduled_shipping_days")
    .withColumnRenamed("Benefit per order", "benefit_per_order")
    .withColumnRenamed("Sales per customer", "sales_per_customer")
    .withColumnRenamed("Delivery Status", "delivery_status")
    .withColumnRenamed("Late_delivery_risk", "late_delivery_risk")
    .withColumnRenamed("Category Id", "category_id")
    .withColumnRenamed("Category Name", "category_name")
    .withColumnRenamed("Customer City", "customer_city")
    .withColumnRenamed("Customer Country", "customer_country")
    .withColumnRenamed("Customer Id", "customer_id")
    .withColumnRenamed("Customer Segment", "customer_segment")
    .withColumnRenamed("Customer State", "customer_state")
    .withColumnRenamed("Customer Zipcode", "customer_zipcode")
    .withColumnRenamed("Department Id", "department_id")
    .withColumnRenamed("Department Name", "department_name")
    .withColumnRenamed("Latitude", "latitude")
    .withColumnRenamed("Longitude", "longitude")
    .withColumnRenamed("Market", "market")
    .withColumnRenamed("Order City", "order_city")
    .withColumnRenamed("Order Country", "order_country")
    .withColumnRenamed("Order Customer Id", "order_customer_id")
    .withColumnRenamed("order date (DateOrders)", "order_date")
    .withColumnRenamed("Order Id", "order_id")
    .withColumnRenamed("Order Item Cardprod Id", "order_item_cardprod_id")
    .withColumnRenamed("Order Item Discount", "order_item_discount")
    .withColumnRenamed("Order Item Discount Rate", "order_item_discount_rate")
    .withColumnRenamed("Order Item Id", "order_item_id")
    .withColumnRenamed("Order Item Product Price", "order_item_product_price")
    .withColumnRenamed("Order Item Profit Ratio", "order_item_profit_ratio")
    .withColumnRenamed("Order Item Quantity", "order_item_quantity")
    .withColumnRenamed("Sales", "sales")
    .withColumnRenamed("Order Item Total", "order_item_total")
    .withColumnRenamed("Order Profit Per Order", "order_profit_per_order")
    .withColumnRenamed("Order Region", "order_region")
    .withColumnRenamed("Order State", "order_state")
    .withColumnRenamed("Order Status", "order_status")
    .withColumnRenamed("Order Zipcode", "order_zipcode")
    .withColumnRenamed("Product Card Id", "product_card_id")
    .withColumnRenamed("Product Category Id", "product_category_id")
    .withColumnRenamed("Product Name", "product_name")
    .withColumnRenamed("Product Price", "product_price")
    .withColumnRenamed("Product Status", "product_status")
    .withColumnRenamed("shipping date (DateOrders)", "shipping_date")
    .withColumnRenamed("Shipping Mode", "shipping_mode")
)


'''
print('Columns:', len(df.columns))
print(df.columns)

df.printSchema()
'''
print("\nSample dates:")

df.select(
    "order_date",
    "shipping_date"
).show(20, truncate=False)

print("\nDate string lengths:")



df.select(
    length("order_date").alias("order_date_length"),
    length("shipping_date").alias("shipping_date_length")
).groupBy(
    "order_date_length",
    "shipping_date_length"
).count().orderBy(
    "order_date_length",
    "shipping_date_length"
).show()



df= (
    df
    .withColumn('order_date', to_timestamp('order_date','M/d/yyyy H:mm'))
    .withColumn('shipping_date', to_timestamp('shipping_date','M/d/yyyy H:mm'))
)



df.select('order_date','shipping_date').show(10, truncate=False)

print('\nDate schema:')

df.select('order_date','shipping_date').printSchema()

spark.stop()