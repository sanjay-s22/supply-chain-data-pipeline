def write_processed_data(
    dim_customer,dim_product,
    dim_date, fact_order_items):

    dim_customer.write.mode('overwrite').parquet(
        'data/processed/dim_customer')

    dim_product.write.mode('overwrite').parquet(
        'data/processed/dim_product')

    dim_date.write.mode('overwrite').parquet(
        'data/processed/dim_date')

    fact_order_items.write.mode('overwrite').parquet(
        'data/processed/fact_order_items')

    print('\n----Data Written----')
    print('processed data written to data/processed')
