import streamlit as st
import pandas as pd
import plotly.express as px

# Leer datos
df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Dashboard de Vehículos Usados')

st.write('Exploración básica del dataset de anuncios de venta de vehículos.')

# Checkbox para histograma
build_hist = st.checkbox('Construir histograma del odómetro')

if build_hist:
    st.write('Histograma de la columna odometer')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión Precio vs Odómetro')

if build_scatter:
    st.write('Gráfico de dispersión entre precio y odómetro')
    fig2 = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)