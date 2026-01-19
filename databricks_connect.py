from databricks.connect import DatabricksSession

# Use the Databricks CLI profile for authentication
spark = (
    DatabricksSession.builder
    .profile("ADB-Field-Eng-DEFAULT")
    .getOrCreate()
)

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)