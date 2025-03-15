import openpyxl
import pandas as pd
from datetime import datetime
import os
import streamlit as st

class SistemaInventario:
    def __init__(self, archivo="inventario.xlsx"):
        if not os.path.exists(archivo):
            from crear_archivo_inicial import crear_archivo_inicial
            crear_archivo_inicial(archivo)
        self.archivo = archivo
        self.workbook = openpyxl.load_workbook(archivo)
        self.sheet = self.workbook["Inventario"]