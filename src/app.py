from routes import poligonos_buenos_aires, principalindex, censo_cliente, mostrar_htmls, mostrar_archivo_html, login, registro, registrando
from flask import Flask,send_from_directory
import os
# llamamos nuestro app
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='static/favicon.ico')

# routes
@app.route('/')
def log():
    return login.login()

@app.route('/registro', methods=['GET','POST'])
def reg():
    return registro.registro()

@app.route('/login', methods=['GET','POST'])
def log2():
    return registrando.principalregistro()

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
    app.run(debug=True)