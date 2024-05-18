from flask import render_template
from database.mongo.conexion import collection

def obtener_datos():
    datos = list(collection.find({}, {'_id': 0}).limit(10))
    #return jsonify(datos)
    return render_template('datos_origen.html', datos=datos)