import os
from dotenv import load_dotenv

load_dotenv()

mongo_usuario = os.getenv('MONGO_USUARIO')
mongo_credencial = os.getenv('MONGO_CREDENCIAL')
mongo_port = os.getenv('MONGO_PORT')
