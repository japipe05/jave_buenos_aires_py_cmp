import os
from dotenv import load_dotenv

load_dotenv()
# variables de entorno de mongo
mongo_usuario = os.getenv('MONGO_USUARIO')
mongo_credencial = os.getenv('MONGO_CREDENCIAL')
mongo_port = os.getenv('MONGO_PORT')

# variables de entorno de PostgreSQL
postgres_user = os.getenv('POSTGRES_USUARIO')
postgres_password = os.getenv('POSTGRES_CREDENCIAL')
postgres_db = os.getenv('POSTGRES_DB')
postgres_port = os.getenv('POSTGRES_PORT')

#Ambiente
app_entorno = os.getenv('APP_ENTORNO')