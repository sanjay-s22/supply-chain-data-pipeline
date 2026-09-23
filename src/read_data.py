
def read_raw_data(spark):
    return spark.read.csv('data/raw/Supplychaindataset.csv',
    header = True, inferSchema = True)