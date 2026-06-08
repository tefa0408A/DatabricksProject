# Carpeta: PrepAmb | Archivo: 01_prep_amb.py
catalog_name = "proyecto_cinema_catalog"

# Creación de Catálogo y Esquemas obligatorios
spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")
spark.sql(f"USE CATALOG {catalog_name}")

esquemas = ["bronze", "silver", "gold"]
for esquema in esquemas:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog_name}.{esquema}")

print("Ambiente de Unity Catalog preparado correctamente.")