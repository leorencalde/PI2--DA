# Dashboard de Siniestros Viales en CABA

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar los siniestros viales ocurridos en la Ciudad Autónoma de Buenos Aires (CABA) entre 2016 y 2021. Utilizando un dataset proporcionado, hemos creado un dashboard interactivo con Streamlit que permite visualizar y explorar los datos de siniestros viales y víctimas, con el fin de ayudar a las autoridades locales a tomar decisiones informadas para reducir la cantidad de víctimas fatales.

## Estructura del Repositorio

- `datasets/`
  - `homicidios.xlsx`: Dataset principal con los datos de siniestros viales y víctimas.
- `scripts/`
  - `create_combined_db.py`: Script para crear la base de datos SQLite y combinar las tablas de hechos y víctimas.
  - `dashboard.py`: Script de Streamlit para generar el dashboard interactivo.
- `EDA/`
  - `EDA_Siniestros_Viales.ipynb`: Análisis Exploratorio de Datos (EDA) del dataset.
- `README.md`: Este archivo, que proporciona una descripción completa del proyecto.

## Tecnologías y Herramientas Utilizadas

- **Python**: Lenguaje de programación principal utilizado para el análisis y la creación del dashboard.
- **Pandas**: Biblioteca utilizada para la manipulación y el análisis de datos.
- **SQLite**: Motor de base de datos utilizado para almacenar los datos de siniestros viales.
- **Streamlit**: Framework utilizado para crear el dashboard interactivo.
- **Matplotlib**: Biblioteca utilizada para la generación de gráficos y visualizaciones.
- **Jupyter Notebook**: Utilizado para el Análisis Exploratorio de Datos (EDA).

## Metodología Aplicada

1. **Análisis Exploratorio de Datos (EDA)**:
   - Se realizó un EDA para comprender la estructura del dataset y explorar las tendencias y patrones de los siniestros viales.
   - El EDA se llevó a cabo en el notebook `EDA_Siniestros_Viales.ipynb`.

2. **Creación de la Base de Datos**:
   - Se creó una base de datos SQLite a partir del dataset proporcionado.
   - El script `create_combined_db.py` se utilizó para cargar los datos, combinarlos y almacenarlos en una base de datos.

3. **Desarrollo del Dashboard**:
   - Se desarrolló un dashboard interactivo utilizando Streamlit para visualizar los datos de siniestros viales y víctimas.
   - El script `dashboard.py` genera el dashboard, permitiendo la exploración de los datos mediante filtros interactivos y visualizaciones gráficas.

## Análisis y Funcionalidad de los KPIs

### KPI 1: Tasa de Homicidios en Siniestros Viales

- **Definición**: Número de víctimas fatales en accidentes de tránsito por cada 100,000 habitantes en CABA.
- **Objetivo**: Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses en comparación con el semestre anterior.
- **Fórmula**: (Número de homicidios en siniestros viales / Población total) * 100,000
- **Implementación**: El dashboard permite calcular y visualizar la tasa de homicidios en siniestros viales, mostrando las tendencias a lo largo del tiempo.

### KPI 2: Cantidad de Accidentes Mortales de Motociclistas

- **Definición**: Número absoluto de accidentes fatales en los que estuvieron involucradas víctimas que viajaban en moto.
- **Objetivo**: Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año respecto al año anterior.
- **Fórmula**: (Número de accidentes mortales con víctimas en moto en el año anterior - Número de accidentes mortales con víctimas en moto en el año actual) / (Número de accidentes mortales con víctimas en moto en el año anterior) * 100
- **Implementación**: El dashboard permite filtrar los datos para identificar y analizar los accidentes mortales de motociclistas, proporcionando visualizaciones claras de las tendencias anuales.

## Reporte de Análisis

El dashboard interactivo proporciona una plataforma intuitiva para explorar los datos de siniestros viales. Los usuarios pueden filtrar los datos por año y mes, visualizar la distribución geográfica de los siniestros y analizar las tendencias de homicidios por edad y tipo de participante.

### Hallazgos Clave

- **Tendencias Temporales**: Se observa un patrón estacional en la ocurrencia de siniestros viales, con picos en ciertos meses del año.
- **Análisis Geoespacial**: Algunas áreas específicas de la ciudad muestran una mayor concentración de siniestros viales.
- **Distribución por Edad y Sexo**: La mayoría de las víctimas fatales son jóvenes adultos, con una proporción significativa de hombres.

Este análisis proporciona una base sólida para que las autoridades locales tomen medidas informadas para mejorar la seguridad vial en CABA.

---

### Contacto

**LEONARDO RENTERIA**  | Email: leo921120@hotmail.com | Telefono: +573138228947 | Ubicación: Bogotá DC |
