from IPython.core.magic import register_line_magic # type: ignore
from pyspark.sql import SparkSession # type: ignore

@register_line_magic
def sql(line):
    return spark.sql(line).show() # type: ignore

print("✅ Custom %sql magic loaded: Run SQL queries with Spark inside Jupyter Notebooks!")
