import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import altair as alt

# Función para cargar y combinar los datos desde la base de datos SQLite
def load_data():
    conn = sqlite3.connect('1. Datasets/siniestros_viales.db')
    
    hechos_df = pd.read_sql_query('SELECT * FROM hechos', conn)
    victimas_df = pd.read_sql_query('SELECT * FROM victimas', conn)
    
    conn.close()
    
    # Eliminar las columnas ALTURA, CRUCE y DIRECCION_NORMALIZADA
    hechos_df.drop(columns=['Altura', 'Cruce', 'Dirección Normalizada'], inplace=True)
    
    # Combinar los datos de hechos y víctimas
    combined_df = pd.merge(hechos_df, victimas_df, left_on='ID', right_on='ID_hecho', how='left')
    
    # Convertir las columnas 'POS_X' y 'POS_Y' a valores numéricos, manejando errores
    combined_df['pos x'] = pd.to_numeric(combined_df['pos x'], errors='coerce')
    combined_df['pos y'] = pd.to_numeric(combined_df['pos y'], errors='coerce')
    
    # Limpiar la columna 'EDAD' convirtiéndola a valores numéricos, manejando errores
    combined_df['EDAD'] = pd.to_numeric(combined_df['EDAD'], errors='coerce')

    # Renombrar las columnas 'POS_Y' y 'POS_X' a 'latitude' y 'longitude'
    combined_df.rename(columns={'pos y': 'latitude', 'pos x': 'longitude'}, inplace=True)
    
    return combined_df

# Cargar los datos
data = load_data()

# Crear el dashboard con Streamlit
st.title('Análisis de Datos de Siniestros Viales en la Ciudad Autónoma de Buenos Aires')

# Filtros de selección
st.sidebar.header('Filtros')
anio = st.sidebar.selectbox('Año', ['Todos'] + sorted(data['AAAA_x'].unique().tolist()))

# Filtrar los datos según los filtros seleccionados
if anio != 'Todos':
    filtered_data = data[data['AAAA_x'] == anio]
else:
    filtered_data = data

# Calcular el número total de siniestros viales
total_siniestros_viales = data['N_VICTIMAS'].sum()

# Mostrar el número total de siniestros viales
st.subheader('Número Total de Siniestros Viales (2016-2021)')
st.metric('Total de Siniestros Viales', total_siniestros_viales)

# Agregar gráfico interactivo del total de siniestros viales
st.subheader('Total de Siniestros Viales (2016-2021)')
total_siniestros = data.groupby(['AAAA_x']).size().reset_index(name='counts')
chart = alt.Chart(total_siniestros).mark_line(point=True).encode(
    x='AAAA_x:O',
    y='counts:Q',
    tooltip=['AAAA_x', 'counts']
).interactive()

st.altair_chart(chart, use_container_width=True)

# Gráfico de incidencia de accidentes en los meses de verano
st.subheader('Incidencia de Accidentes por Mes')
monthly_accidents = filtered_data.groupby(['AAAA_x', 'MM_x']).size().reset_index(name='counts')
monthly_chart = alt.Chart(monthly_accidents).mark_bar().encode(
    x=alt.X('MM_x:O', title='Mes'),
    y=alt.Y('counts:Q', title='Total de Siniestros'),
    color='AAAA_x:N',
    tooltip=['AAAA_x', 'MM_x', 'counts']
).properties(
    title='Incidencia de Accidentes por Mes'
).interactive()

st.altair_chart(monthly_chart, use_container_width=True)

# KPI 1: Tasa de homicidios en siniestros viales
poblacion_total = 3075646  # Población de CABA
num_homicidios = filtered_data['ID_hecho'].nunique()
tasa_homicidios = (num_homicidios / poblacion_total) * 100000
st.metric('Tasa de Homicidios en Siniestros Viales', f'{tasa_homicidios:.2f} por 100,000 habitantes')

# KPI 2: Cantidad de accidentes mortales de motociclistas
num_accidentes_motos = filtered_data[filtered_data['VICTIMA_y'] == 'MOTO']['ID_hecho'].nunique()
st.metric('Accidentes Mortales de Motociclistas', num_accidentes_motos)

# Visualización de los datos
st.subheader('Mapa de Siniestros Viales')
st.map(filtered_data[['latitude', 'longitude']])

st.subheader('Distribución de Homicidios por Edad y Sexo')
fig, ax = plt.subplots()
filtered_data['EDAD'].hist(ax=ax, bins=30)
ax.set_xlabel('Edad')
ax.set_ylabel('Cantidad')
st.pyplot(fig)

st.subheader('Homicidios por Tipo de Participante')
fig, ax = plt.subplots()
filtered_data['VICTIMA_y'].value_counts().plot(kind='bar', ax=ax)
ax.set_xlabel('Tipo de Participante')
ax.set_ylabel('Cantidad')
st.pyplot(fig)

# Agregar gráfico de barras para visualizar KPIs
st.subheader('Comparación de KPIs a lo largo del tiempo')
kpi_data = filtered_data.groupby(['AAAA_x', 'MM_x']).agg({
    'ID_hecho': 'nunique',
    'VICTIMA_y': lambda x: (x == 'MOTO').sum()
}).reset_index()

fig, ax = plt.subplots()
kpi_data.plot(kind='bar', x='AAAA_x', y=['ID_hecho', 'VICTIMA_y'], ax=ax)
ax.set_xlabel('Año')
ax.set_ylabel('Cantidad')
st.pyplot(fig)
