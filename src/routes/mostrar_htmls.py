import os
from flask import  render_template
# Ruta de la carpeta donde se encuentran los archivos HTML
carpeta_outputs = "outputs"
def mostrar_htmls():
    # Obtener la lista de archivos HTML en la carpeta "outputs"
    archivos_html = [f for f in os.listdir(carpeta_outputs) if f.endswith('.html')]
    return render_template('listadosweb.html', archivos_html=archivos_html)