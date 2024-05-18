import os
import pandas as pd
from pymongo import MongoClient
import xlrd

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv()

MONGO_USUARIO = os.getenv('MONGO_USUARIO')
MONGO_CREDENCIAL = os.getenv('MONGO_CREDENCIAL')
MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))

# Conectar a MongoDB
client = MongoClient(f'mongodb://{MONGO_USUARIO}:{MONGO_CREDENCIAL}@localhost:{MONGO_PORT}/')
db = client['mi_basededatos']

# Crear la colección si no existe
collection = db['coleccion_mongo_jave']

# Leer el archivo Excel
workbook = xlrd.open_workbook('insumos/reporte.xls')
sheet = workbook.sheet_by_index(0)

# Convertir el contenido del Excel a una lista de diccionarios
data = []
for row_index in range(1, sheet.nrows):  # Empezar desde la segunda fila para ignorar los encabezados
    row = sheet.row_values(row_index)
    data.append({
        'campo1': row[0],  # Reemplaza 'campo1', 'campo2', etc. con los nombres reales de tus columnas
        'campo2': row[1],
        # Agrega más campos según sea necesario
    })

# Subir los datos a MongoDB
collection.insert_many(data)

print("Datos subidos correctamente.")
