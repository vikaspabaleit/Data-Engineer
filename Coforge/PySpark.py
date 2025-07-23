# How would you read a large CSV file in chunks, filter only required rows, and write the output into a new file using Python
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.bulder.appName("Read CSV File").getOrCreate()

#Read CSV file
df = spark.read.csv("large_input.csv", header=True, InferSchema=True)
df.printSchema()

#Filter the data
filtered_df = df.filter([df['column_name'] > 100)

# Write to output file
filtered_df.write.csv("large_output.csv", header=True, mode="overwrite")

# Stop Spark session
spark.stop()
