from pymongo import MongoClient
from config.envs import mongo_usuario, mongo_credencial, mongo_port
from config.envs import  app_entorno

if app_entorno == 'DESARROLLO':
    mongo_client = MongoClient(f'mongodb://{mongo_usuario}:{mongo_credencial}@localhost:{mongo_port}/')
else:
    mongo_client = MongoClient(f'mongodb://{mongo_usuario}:{mongo_credencial}@mongo:{mongo_port}/') #Docker

db = mongo_client['db_javeriana']
collection = db['poligonos_buenos_aires']
