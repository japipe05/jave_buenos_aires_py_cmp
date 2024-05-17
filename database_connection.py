import os
from cassandra.cluster import Cluster
from pymongo import MongoClient
import psycopg2
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Conexión a Cassandra
def connect_to_cassandra():
    cluster = Cluster([os.getenv('CASSANDRA_CONTAINER_NAME')])
    session = cluster.connect()
    return session

# Conexión a MongoDB
def connect_to_mongodb():
    client = MongoClient(f"mongodb://{os.getenv('MONGO_INITDB_ROOT_USERNAME')}:{os.getenv('MONGO_INITDB_ROOT_PASSWORD')}@localhost:{os.getenv('MONGO_PORT')}/?authSource=admin")
    db = client[os.getenv('MONGO_INITDB_DATABASE')]
    return db

# Conexión a PostGIS
def connect_to_postgis():
    conn = psycopg2.connect(
        dbname=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host='localhost',
        port=os.getenv('POSTGRES_PORT')
    )
    return conn

# Ejemplo de uso
if __name__ == "__main__":
    # Conexión a Cassandra
    cassandra_session = connect_to_cassandra()
    print("Conexión a Cassandra establecida.")

    # Conexión a MongoDB
    mongodb_db = connect_to_mongodb()
    print("Conexión a MongoDB establecida.")

    # Conexión a PostGIS
    postgis_conn = connect_to_postgis()
    print("Conexión a PostGIS establecida.")
