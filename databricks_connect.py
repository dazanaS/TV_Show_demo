import os
from pathlib import Path
from dotenv import load_dotenv
from databricks.connect import DatabricksSession

# Load environment variables from .databricks/.databricks.env
env_path = Path(__file__).parent / '.databricks' / '.databricks.env'
load_dotenv(env_path)

spark = DatabricksSession.builder.getOrCreate()

df = spark.read.table("samples.nyctaxi.trips")
df.show(5)