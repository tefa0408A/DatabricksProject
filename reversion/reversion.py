# Carpeta: reversion | Archivo: reversion.py
catalog_name = "proyecto_cinema_catalog"

print("Iniciando proceso de reversión...")
spark.sql(f"DROP TABLE IF EXISTS {catalog_name}.gold.fact_director_performance")
spark.sql(f"DROP TABLE IF EXISTS {catalog_name}.silver.dim_movies_master")
spark.sql(f"DROP TABLE IF EXISTS {catalog_name}.bronze.stg_film_details")
spark.sql(f"DROP TABLE IF EXISTS {catalog_name}.bronze.stg_movies")

print("Tablas removidas de manera lógica y física.")