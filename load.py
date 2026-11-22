from sqlalchemy import create_engine
import psycopg2
import config as c

db_name = c.DB_NAME
user = c.DB_USER
password = c.DB_PASSWORD
host = c.DB_HOST
port = c.DB_PORT

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

def load(df, table_name):
    
    df.to_sql(table_name,
              engine,
              if_exists = 'replace',
              index = False)
    
    print('Data loaded successfully')