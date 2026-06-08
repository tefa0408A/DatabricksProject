-- Carpeta: seguridad | Archivo: grants.sql
USE CATALOG proyecto_cinema_catalog;

-- Otorgar permisos de lectura al equipo de Analistas de Datos en la capa Gold
GRANT USAGE ON CATALOG proyecto_cinema_catalog TO `analyst_group`;
GRANT USAGE ON SCHEMA gold TO `analyst_group`;
GRANT SELECT ON TABLE gold.fact_director_performance TO `analyst_group`;

-- Otorgar permisos totales al equipo de Data Engineering
GRANT ALL PRIVILEGES ON CATALOG proyecto_cinema_catalog TO `data_engineers_group`;