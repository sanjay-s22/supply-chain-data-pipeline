import pandas as pd 

file_path = 'data/raw/Supplychaindataset.csv'
df = pd.read_csv(file_path, encoding='latin-1')

print('rows:', len(df))
print('columns:', len(df.columns))

print('\nColumns:')
print(df.columns.tolist())

print('\nData types:')
print(df.dtypes)

print('\nMissing values:')
print(df.isnull().sum())

print('\nduplicate rows:', df.duplicated().sum())

print("\nUnique values:")

print("Orders:", df["Order Id"].nunique())
print("Order items:", df["Order Item Id"].nunique())
print("Customers:", df["Customer Id"].nunique())
print("Products:", df["Product Card Id"].nunique())
print("Categories:", df["Category Id"].nunique())
print("Departments:", df["Department Id"].nunique())

print("\nOrder statuses:")
print(df["Order Status"].value_counts())

print("\nShipping modes:")
print(df["Shipping Mode"].value_counts())

print("\nMarkets:")
print(df["Market"].value_counts())

print("\nDate range:")
print("Start:", df["order date (DateOrders)"].min())
print("End:", df["order date (DateOrders)"].max())
