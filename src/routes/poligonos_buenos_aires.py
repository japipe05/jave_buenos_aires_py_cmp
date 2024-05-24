from flask import render_template
from database.mongo.conexion import collection
from flask import jsonify
from models.poligonos_buenos_aires import crear_coleccion_si_no_existe, insertar_registros_desde_csv

def obtener_datos():
    crear_coleccion_si_no_existe()
    insertar_registros_desde_csv()
    datos = list(collection.find({}, {'_id': 0}).limit(10))
    #return jsonify(datos)
    return render_template('poligonos_buenos_aires.html', datos=datos)

def obtener_all():
    datos = list(collection.find({}, {'_id': 0}))
    return jsonify(datos)

def obtener_limit2():
    datos = list(collection.find({}, {'_id': 0}).limit(10))
    return jsonify(datos)
              