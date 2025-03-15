import streamlit as st

def actualizar_cantidad(sistema, producto, nueva_cantidad):
    for row in range(2, sistema.sheet.max_row + 1):
        if sistema.sheet.cell(row=row, column=1).value == producto:
            sistema.sheet.cell(row=row, column=2).value = nueva_cantidad
            sistema.workbook.save(sistema.archivo)
            st.success(f"Cantidad actualizada para {producto}.")
            return
    st.error("Producto no encontrado.")