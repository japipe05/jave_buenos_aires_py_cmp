# Conexión a la base de datos
from sqlalchemy import create_engine
from config.envs import postgres_user, postgres_password, postgres_db,postgres_port
from config.envs import  app_entorno

if app_entorno == 'DESARROLLO':
    POSTGRES_HOST = '127.0.0.2'
else:
    POSTGRES_HOST = 'db' #docker
    
engine = create_engine(f'postgresql://{postgres_user}:{postgres_password}@{POSTGRES_HOST}:{postgres_port}/{postgres_db}')
