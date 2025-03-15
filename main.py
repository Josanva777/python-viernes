import streamlit as st
from sistema_inventario import SistemaInventario
from registrar_producto import registrar_producto
from actualizar_cantidad import actualizar_cantidad
from generar_reporte import generar_reporte
from visualizar_estadisticas import visualizar_estadisticas
from resetear_inventario import resetear_inventario

def main():
    sistema = SistemaInventario()
    st.title("Sistema de Gestión de Inventarios")

    menu = ["Registrar producto", "Actualizar cantidad", "Generar reporte", "Visualizar estadísticas", "Resetear inventario", "Salir"]
    choice = st.sidebar.selectbox("Menú", menu)

    if choice == "Registrar producto":
        st.subheader("Registrar producto")
        producto = st.text_input("Nombre del producto")
        cantidad = st.number_input("Cantidad", min_value=0, step=1)
        precio_unitario = st.number_input("Precio unitario", min_value=0.0, step=0.01)
        if st.button("Registrar"):
            registrar_producto(sistema, producto, cantidad, precio_unitario)

    elif choice == "Actualizar cantidad":
        st.subheader("Actualizar cantidad")
        producto = st.text_input("Nombre del producto")
        nueva_cantidad = st.number_input("Nueva cantidad", min_value=0, step=1)
        if st.button("Actualizar"):
            actualizar_cantidad(sistema, producto, nueva_cantidad)

    elif choice == "Generar reporte":
        st.subheader("Generar reporte")
        generar_reporte(sistema)

    elif choice == "Visualizar estadísticas":
        st.subheader("Visualizar estadísticas")
        visualizar_estadisticas(sistema)

    elif choice == "Resetear inventario":
        st.subheader("Resetear inventario")
        if st.button("Resetear"):
            resetear_inventario(sistema)

    elif choice == "Salir":
        st.subheader("Salir")
        st.write("¡Hasta luego!")

if __name__ == "__main__":
    main()