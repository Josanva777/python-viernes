import pandas as pd
import streamlit as st

def visualizar_estadisticas(sistema):
    df = pd.read_excel(sistema.archivo)
    estadisticas = df.groupby("Producto")["Cantidad"].sum().dropna()
    if estadisticas.empty:
        st.warning("No hay datos para mostrar estadísticas.")
        return
    st.bar_chart(estadisticas)