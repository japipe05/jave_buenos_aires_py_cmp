import os
from flask import render_template
# Ruta de la carpeta donde se encuentran los archivos HTML
carpeta_outputs = "outputs"
def mostrar_archivo_html(nombre_archivo):
    ruta_archivo = os.path.join(carpeta_outputs, nombre_archivo)
    with open(ruta_archivo, 'r') as file:
        contenido = file.read()
    return render_template('contenidoweb.html', contenido=contenido)