from sqlalchemy import create_engine, text
import logging
import config as c

logger = logging.getLogger(__name__)

db_name = c.DB_NAME
user = c.DB_USER
password = c.DB_PASSWORD
host = c.DB_HOST
port = c.DB_PORT

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

def load(df, table_name):
    try:
        logger.info('Loading data')
        df.to_sql('weather_staging',
                engine,
                if_exists = 'replace',
                index = False)
        with engine.begin() as conn:
            conn.execute(text("""
                INSERT INTO weather (datetime, temp, windspeed, humidity, pressure, conditions, city)
                SELECT datetime, temp, windspeed, humidity, pressure, conditions, city FROM weather_staging
                ON CONFLICT (city, datetime) DO UPDATE SET
                    temp = EXCLUDED.temp,
                    windspeed = EXCLUDED.windspeed,
                    humidity = EXCLUDED.humidity,
                    pressure = EXCLUDED.pressure,
                    conditions = EXCLUDED.conditions
            """))
        logger.info('Data loaded succesfully')
    except:
        logger.exception('Data loading failed')
            