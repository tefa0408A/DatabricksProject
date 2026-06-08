# Carpeta: proceso | Archivo: 02_extract_bronze.py
from pyspark.sql.functions import current_timestamp, input_file_name

catalog_name = "proyecto_cinema_catalog"

# Rutas simuladas a tu cuenta de almacenamiento Azure Blob Storage/ADLS Gen2 con Managed Identity
ruta_raw_movies = "abfss://raw@tu_storage_account.dfs.core.windows.net/Movies.csv"
ruta_raw_details = "abfss://raw@tu_storage_account.dfs.core.windows.net/FilmDetails.csv"

# Ingesta estricta con PySpark
df_movies = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(ruta_raw_movies)

df_details = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(ruta_raw_details)

# Adición de metadatos de auditoría
df_movies_bronze = df_movies.withColumn("fecha_ingesta", current_timestamp()) \
                            .withColumn("origen_archivo", input_file_name())

df_details_bronze = df_details.withColumn("fecha_ingesta", current_timestamp()) \
                              .withColumn("origen_archivo", input_file_name())

# Escritura en tablas Delta de la capa Bronze
df_movies_bronze.write.format("delta").mode("overwrite") \
    .saveAsTable(f"{catalog_name}.bronze.stg_movies")

df_details_bronze.write.format("delta").mode("overwrite") \
    .saveAsTable(f"{catalog_name}.bronze.stg_film_details")

print("Capa Bronze cargada exitosamente.")