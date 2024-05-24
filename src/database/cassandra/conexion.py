from cassandra.cluster import Cluster
from config.envs import  app_entorno

if app_entorno == 'DESARROLLO':
   #cluster = Cluster(['127.0.0.1'])
   cluster = Cluster(['localhost'])  
else:
    cluster = Cluster(['cassandra']) #docker

session = cluster.connect()

import os

session.execute("CREATE KEYSPACE IF NOT EXISTS topicos WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE topicos")
session.execute("CREATE TABLE IF NOT EXISTS topicos.users ( credencial text, usuario text,PRIMARY KEY ( usuario))")