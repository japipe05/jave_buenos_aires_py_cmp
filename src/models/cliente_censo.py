import pandas as pd
from database.mongo.conexion import collection, db

def crear_coleccion_si_no_existe():
    if 'cliente_censo' not in db.list_collection_names():
        db.create_collection('cliente_censo')

def insertar_registros_desde_csv():
    df = pd.read_csv('insumos/df_census.csv')
    records = df.to_dict(orient='records')
    collection.insert_many(records)
