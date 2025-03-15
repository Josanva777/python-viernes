import openpyxl

def crear_archivo_inicial(archivo):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Inventario"
    headers = ["Producto", "Cantidad", "Precio Unitario", "Fecha de Registro"]
    sheet.append(headers)
    wb.save(archivo)