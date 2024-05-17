from cassandra.cluster import Cluster

# Configura el contacto inicial con un nodo de Cassandra
cluster = Cluster(['cassandra1', 'cassandra2', 'cassandra3'])

# Conecta con el cluster y abre una sesión
session = cluster.connect()

# Crea un keyspace y una tabla (solo si es necesario)
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS test_keyspace
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
""")
session.set_keyspace('test_keyspace')

session.execute("""
    CREATE TABLE IF NOT EXISTS test_table (
        id int PRIMARY KEY,
        name text
    );
""")

# Inserta datos en la tabla
session.execute("INSERT INTO test_table (id, name) VALUES (%s, %s)", (1, 'John'))
session.execute("INSERT INTO test_table (id, name) VALUES (%s, %s)", (2, 'Alice'))

# Consulta datos de la tabla
rows = session.execute("SELECT * FROM test_table")
for row in rows:
    print(row.id, row.name)

# Cierra la sesión y el cluster al finalizar
session.shutdown()
cluster.shutdown()
