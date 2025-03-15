# Proyecto de Gestión de Inventarios

## Descripción
Este proyecto es un sistema de gestión de inventarios que permite registrar productos, actualizar cantidades, generar reportes de inventario y visualizar estadísticas de ventas.

## Instrucciones de Instalación y Configuración
1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea y activa el entorno virtual:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # En Windows
    source .venv/bin/activate  # En macOS y Linux
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

## Guía de Uso
1. Ejecuta el script principal:
    ```sh
    streamlit run main.py
    ```

2. Sigue las instrucciones en pantalla para registrar productos, actualizar cantidades, generar reportes y visualizar estadísticas.

## Dependencias Utilizadas
- openpyxl
- pandas
- matplotlib
- streamlit

## Contribuciones
- **Johan Sánchez**: Implementación de la funcionalidad de registro de productos.
- **José Toro**: Desarrollo de la actualización de cantidades.
- **Sebastian Vasquez**: Creación de la generación de reportes de inventario.
- **Sebastian Jimenez**: Visualización de estadísticas de ventas y documentación.






Johan Sánchez: Trabaja en el archivo registrar_producto.py.
José Toro: Trabaja en el archivo actualizar_cantidad.py.
Sebastian Vasquez: Trabaja en el archivo generar_reporte.py.
Sebastian Jimenez: Trabaja en los archivos visualizar_estadisticas.py y resetear_inventario.py.