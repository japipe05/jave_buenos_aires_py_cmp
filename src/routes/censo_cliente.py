from models.censo_clientes import consultar_datos
from flask import render_template
from models.censo_clientes import cargar_csv_to_db
def censo_cliente():
    cargar_csv_to_db()
    # Consultar los datos y devolverlos en HTML
    tabla_html = consultar_datos()
    return render_template('censo_cliente.html', tabla=tabla_html)