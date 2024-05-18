from flask import Flask, jsonify
import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from flask import render_template

# Cargar variables de entorno desde el archivo .env
load_dotenv()


app = Flask(__name__)

# Obtener variables de entorno
mongo_usuario = os.getenv('MONGO_USUARIO')
mongo_credencial = os.getenv('MONGO_CREDENCIAL')
mongo_port = os.getenv('MONGO_PORT')

print(mongo_usuario)
print(mongo_credencial)
print(mongo_port)

# Conexión a MongoDB
mongo_client = MongoClient(f'mongodb://{mongo_usuario}:{mongo_credencial}@localhost:{mongo_port}/')
db = mongo_client['db_javeriana']
collection = db['cliente']


def crear_coleccion_si_no_existe():
    if 'cliente' not in db.list_collection_names():
        db.create_collection('cliente')


def insertar_registros_desde_csv():
    df = pd.read_csv('insumos/df_census.csv')
    records = df.to_dict(orient='records')
    collection.insert_many(records)


@app.route('/datos', methods=['GET'])
def obtener_datos():
    datos = list(collection.find({}, {'_id': 0}))
    return render_template('datos.html', datos=datos)


if __name__ == '__main__':
    crear_coleccion_si_no_existe()
    insertar_registros_desde_csv()
    app.run(debug=True)
