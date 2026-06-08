# Pipeline End-to-End: Arquitectura Medallion en Databricks

## Arquitectura del Proyecto
Este repositorio contiene un flujo de datos ETL automatizado implementado en Azure Databricks utilizando PySpark puro para procesar información cinematográfica compleja.

1. **Capa Raw:** Archivos planos almacenados de forma externa en Azure ADLS Gen2, consumidos estrictamente mediante **Managed Identity**.
2. **Capa Bronze:** Ingesta de datos crudos agregando columnas de auditoría temporal (`stg_movies`, `stg_film_details`).
3. **Capa Silver:** Limpieza de datos duplicados, tipado explícito y unión lógica relacional (`dim_movies_master`).
4. **Capa Gold:** Generación de métricas de negocio agregadas y optimizadas para consumo analítico (`fact_director_performance`).

## Estructura de Orquestación CI/CD
El despliegue está automatizado vía GitHub Actions configurando ejecuciones secuenciales controladas por pasos lógicos desde el entorno de desarrollo hasta el catálogo de producción.
