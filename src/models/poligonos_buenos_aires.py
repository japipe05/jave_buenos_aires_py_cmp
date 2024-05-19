from database.mongo.conexion import collection, db
import json

def crear_coleccion_si_no_existe():
    if 'poligonos_buenos_aires' not in db.list_collection_names():
        db.create_collection('poligonos_buenos_aires')

def insertar_registros_desde_csv():
    archivo='insumos/RMBA.geojson'
    with open(archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
    collection.insert_many(data['features'])

