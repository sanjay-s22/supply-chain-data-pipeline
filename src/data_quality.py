def run_quality_checks(df):

    print("\n=== DATA QUALITY CHECKS ===")

    print("\nNull counts:")

    for column in df.columns:
        count = df.filter(df[column].isNull()).count()

        if count > 0:
            print(f"{column}: {count}")

    print("\nUnique IDs:")

    print("Orders:", df.select("order_id").distinct().count())
    print("Order items:", df.select("order_item_id").distinct().count())
    print("Customers:", df.select("customer_id").distinct().count())
    print("Products:", df.select("product_card_id").distinct().count())

    print("\nDuplicate order_item_id:")

    duplicate_items = (
        df.groupBy("order_item_id")
        .count()
        .filter("count > 1")
        .count()
    )

    print(duplicate_items)

    print("\nCustomer ID consistency:")

    customer_mismatch = (
        df.filter(
            df.customer_id != df.order_customer_id
        ).count()
    )

    print(customer_mismatch)

    print("\nCategory ID consistency:")

    category_mismatch = (
        df.filter(
            df.category_id != df.product_category_id
        ).count()
    )

    print(category_mismatch)


def check_fact_table(fact):

    print("\n=== FACT TABLE CHECKS ===")

    print("Rows:", fact.count())

    print(
        "Null customer keys:",
        fact.filter(fact.customer_key.isNull()).count()
    )

    print(
        "Null product keys:",
        fact.filter(fact.product_key.isNull()).count()
    )

    print(
        "Null date keys:",
        fact.filter(fact.date_key.isNull()).count()
    )

    print(
        "Duplicate order_item_id:",
        fact.groupBy("order_item_id")
        .count()
        .filter("count > 1")
        .count())