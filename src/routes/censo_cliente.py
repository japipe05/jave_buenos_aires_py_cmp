from models.censo_clientes import consultar_datos
from flask import render_template
def censo_cliente():
    # Consultar los datos y devolverlos en HTML
    tabla_html = consultar_datos()
    return render_template('censo_cliente.html', tabla=tabla_html)