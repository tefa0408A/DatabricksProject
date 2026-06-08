# Carpeta: proceso | Archivo: 04_load_gold.py
from pyspark.sql.functions import col, sum, avg, count, round

catalog_name = "proyecto_cinema_catalog"

df_silver = spark.table(f"{catalog_name}.silver.dim_movies_master")

# Regla de Negocio: Rentabilidad y rendimiento por Director
df_gold_directores = df_silver.groupBy("director") \
    .agg(
        count("id").alias("total_peliculas"),
        round(avg("score_usuario"), 2).alias("score_promedio"),
        sum("presupuesto_usd").alias("inversion_total_usd"),
        sum("ingresos_usd").alias("recaudacion_total_usd"),
        sum(col("ingresos_usd") - col("presupuesto_usd")).alias("ganancia_neta_total_usd")
    ) \
    .filter(col("director").isNotNull()) \
    .orderBy(col("ganancia_neta_total_usd").desc())

# Persistencia en capa Gold
df_gold_directores.write.format("delta").mode("overwrite") \
    .saveAsTable(f"{catalog_name}.gold.fact_director_performance")

print("Capa Gold procesada con éxito.")