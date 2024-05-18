from models.cliente_censo import crear_coleccion_si_no_existe,insertar_registros_desde_csv
from routes import datos_censo,principalindex
from flask import Flask

from flask import render_template

#llamamos nuestro app
app = Flask(__name__)

#routes
@app.route('/datos_censo', methods=['GET'])
def obtener_datos():
    return datos_censo.obtener_datos()

@app.route('/', methods=['GET'])
def principal():
    #return render_template('index.html')
    return principalindex.principalindex()

# principal
if __name__ == '__main__':
    crear_coleccion_si_no_existe()
    insertar_registros_desde_csv()
    app.run(debug=True)

