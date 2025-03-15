import openpyxl
import streamlit as st
from crear_archivo_inicial import crear_archivo_inicial

def resetear_inventario(sistema):
    crear_archivo_inicial(sistema.archivo)
    sistema.workbook = openpyxl.load_workbook(sistema.archivo)
    sistema.sheet = sistema.workbook["Inventario"]
    st.success("Inventario reseteado con éxito.")