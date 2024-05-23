from database.postgres.conexion import engine
import pandas as pd

# Cargar el archivo df_census.csv en la base de datos
def cargar_csv_to_db():
    df = pd.read_csv('insumos/df_census.csv')
    df.to_sql('census_data', engine, if_exists='replace', index=False)

# Consultar los datos de la base de datos
def consultar_datos():
    query = "SELECT * FROM census_data limit 20"
    df = pd.read_sql(query, engine)
    datos = df.to_dict(orient='records')
    return datos

def consultar_all():
    query = "SELECT * FROM census_data"
    df = pd.read_sql(query, engine)
    return df.to_html(index=False)