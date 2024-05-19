from cassandra.cluster import Cluster
from models.login import hash_password
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
import os
session.execute("CREATE KEYSPACE IF NOT EXISTS topicos WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}")
session.execute("USE topicos")
session.execute("CREATE TABLE IF NOT EXISTS topicos.users ( credencial text, usuario text,PRIMARY KEY ( usuario))")

Usejave = hash_password('jave2024').hex()
session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', 'felipe')")
session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', '3224612380')")

session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', 'oscar')")
session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', '3228344230')")
