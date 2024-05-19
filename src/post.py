from flask import Flask, render_template
import pandas as pd
from sqlalchemy import create_engine

# Configuración de la conexión a la base de datos PostgreSQL
POSTGRES_USER = 'felipe'
POSTGRES_PASSWORD = '2135654felipedsaf54654aAndressdf545'
POSTGRES_DB = 'jave_database'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'

# Conexión a la base de datos
engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')

# Cargar el archivo df_census.csv en la base de datos
def cargar_csv_to_db():
    df = pd.read_csv('insumos/df_census.csv')
    df.to_sql('census_data', engine, if_exists='replace', index=False)

# Consultar los datos de la base de datos
def consultar_datos():
    query = "SELECT * FROM census_data"
    df = pd.read_sql(query, engine)
    return df.to_html(index=False)

app = Flask(__name__)

@app.route('/')
def mostrar_tabla():
    # Cargar datos si no están en la base de datos
    cargar_csv_to_db()
    # Consultar los datos y devolverlos en HTML
    tabla_html = consultar_datos()
    return render_template('censo_cliente.html', tabla=tabla_html)

if __name__ == '__main__':
    app.run(debug=True)
