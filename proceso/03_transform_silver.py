# Carpeta: proceso | Archivo: 03_transform_silver.py
from pyspark.sql.functions import col, coalesce, lit, to_date

catalog_name = "proyecto_cinema_catalog"

# Carga de tablas Bronze
movies_bronze = spark.table(f"{catalog_name}.bronze.stg_movies")
details_bronze = spark.table(f"{catalog_name}.bronze.stg_film_details")

# Transformaciones, Limpieza y Join por la columna 'id'
df_silver = movies_bronze.join(details_bronze, on="id", how="inner") \
    .select(
        col("id").cast("int"),
        col("title").alias("titulo"),
        col("genres").alias("generos"),
        col("language").alias("idioma_original"),
        to_date(col("release_date"), "yyyy-MM-dd").alias("fecha_estreno"),
        col("user_score").cast("double").alias("score_usuario"),
        col("director"),
        col("top_billed").alias("reparto_principal"),
        coalesce(col("budget_usd").cast("double"), lit(0.0)).alias("presupuesto_usd"),
        coalesce(col("revenue_usd").cast("double"), lit(0.0)).alias("ingresos_usd")
    ) \
    .dropDuplicates(["id"])

# Persistencia en capa Silver
df_silver.write.format("delta").mode("overwrite") \
    .saveAsTable(f"{catalog_name}.silver.dim_movies_master")

print("Capa Silver transformada y guardada.")