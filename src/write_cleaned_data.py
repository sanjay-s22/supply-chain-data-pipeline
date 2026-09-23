def write_cleaned_data(df):
    output_path = "data/processed/cleaned_order_items"

    df.write.mode("overwrite").parquet(output_path)

    print(f"\n---- Cleaned Data Written ----")
    print(f"Output: {output_path}")
