# Conexión a la base de datos
from sqlalchemy import create_engine
from config.envs import postgres_user, postgres_password, postgres_db,postgres_port
POSTGRES_HOST = 'localhost'
engine = create_engine(f'postgresql://{postgres_user}:{postgres_password}@{POSTGRES_HOST}:{postgres_port}/{postgres_db}')
