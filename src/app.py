from models.poligonos_buenos_aires import crear_coleccion_si_no_existe, insertar_registros_desde_csv
from models.censo_clientes import cargar_csv_to_db
from routes import poligonos_buenos_aires, principalindex, censo_cliente, mostrar_htmls, mostrar_archivo_html, login
from flask import Flask

# llamamos nuestro app
app = Flask(__name__)

# routes
@app.route('/')
def log():
    return login.login()

@app.route('/home', methods=['POST'])
def principal():
    return principalindex.principalindex()

@app.route('/poligonos_buenos_aires', methods=['GET'])
def obtener_datos():
    return poligonos_buenos_aires.obtener_datos()

@app.route('/censo_cliente', methods=['GET'])
def mostrar_cliente():
    return censo_cliente.censo_cliente()

@app.route('/listadosweb', methods=['GET'])
def htmls():
    return mostrar_htmls.mostrar_htmls()

@app.route('/<nombre_archivo>', methods=['GET'])
def archivohtml(nombre_archivo):
    return mostrar_archivo_html.mostrar_archivo_html(nombre_archivo)


# principal
if __name__ == '__main__':
    crear_coleccion_si_no_existe()
    insertar_registros_desde_csv()
    cargar_csv_to_db()
    app.run(debug=True)