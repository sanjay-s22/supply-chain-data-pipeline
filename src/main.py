from src.spark_session import get_spark 
from src.read_data import read_raw_data
from src.clean_data import clean_data
from src.data_quality import (run_quality_checks, check_fact_table) 
from src.transform import (create_dim_customer, create_dim_product,
 create_dim_date, create_fact_order_items)
from src.write_data import write_processed_data
from src.write_cleaned_data import write_cleaned_data



def main():
    spark = get_spark()
    
    #read
    df = read_raw_data(spark)
    print('Raw columns:', len(df.columns))

    #clean
    df = clean_data(df)
    print('Cleaned columns:', len(df.columns))

    write_cleaned_data(df)

    #quality checks
    run_quality_checks(df)

    #customer dimension
    dim_customer = create_dim_customer(df)

    print('\n==DIM CUSTOMER==')
    print('Rows:', dim_customer.count())

    dim_customer.printSchema()
    dim_customer.show(10, truncate = False)

    #product dimension
    dim_product = create_dim_product(df)

    print("\n=== DIM PRODUCT ===")
    print("Rows:", dim_product.count())
    
    dim_product.printSchema()
    dim_product.show(10, truncate=False)

    #date dimension
    dim_date = create_dim_date(df)

    print("\n=== DIM DATE ===")
    print("Rows:", dim_date.count())

    dim_date.printSchema()
    dim_date.show(10, truncate=False)


    fact_order_items = create_fact_order_items(
    df,
    dim_customer,
    dim_product,
    dim_date)

    print("\n=== FACT ORDER ITEMS ===")
    print("Rows:", fact_order_items.count()) 
    
    fact_order_items.printSchema()
    fact_order_items.show(10, truncate=False)
    check_fact_table(fact_order_items)

    write_processed_data(
        dim_customer,
        dim_product,
        dim_date,
        fact_order_items
    )

    spark.stop()

if __name__ == '__main__':
    main()