from datetime import datetime
import streamlit as st

def registrar_producto(sistema, producto, cantidad, precio_unitario):
    fecha_registro = datetime.now().strftime("%Y-%m-%d")
    sistema.sheet.append([producto, cantidad, precio_unitario, fecha_registro])
    sistema.workbook.save(sistema.archivo)
    st.success(f"Producto {producto} registrado con éxito.")