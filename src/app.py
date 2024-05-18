from models.poligonos_buenos_aires import crear_coleccion_si_no_existe,insertar_registros_desde_csv
from routes import poligonos_buenos_aires,principalindex
from flask import Flask

from flask import render_template

#llamamos nuestro app
app = Flask(__name__)

#routes
@app.route('/poligonos_buenos_aires', methods=['GET'])
def obtener_datos():
    return poligonos_buenos_aires.obtener_datos()

@app.route('/', methods=['GET'])
def principal():
    #return render_template('index.html')
    return principalindex.principalindex()

# principal
if __name__ == '__main__':
    crear_coleccion_si_no_existe()
    insertar_registros_desde_csv()
    app.run(debug=True)

