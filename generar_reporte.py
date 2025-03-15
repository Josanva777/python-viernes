import pandas as pd
import streamlit as st

def generar_reporte(sistema):
    df = pd.read_excel(sistema.archivo)
    st.dataframe(df)