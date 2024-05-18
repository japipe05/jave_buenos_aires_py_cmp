from pymongo import MongoClient
from config.envs import mongo_usuario, mongo_credencial, mongo_port

mongo_client = MongoClient(f'mongodb://{mongo_usuario}:{mongo_credencial}@localhost:{mongo_port}/')
db = mongo_client['db_javeriana']
collection = db['cliente_censo']
