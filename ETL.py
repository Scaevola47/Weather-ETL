import logging
import pandas as pd
from extract import extract_weather
from load import load
from transform import transform_weather

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
)

logger = logging.getLogger(__name__)
CITIES = ['Slupsk', 'Warsaw', 'Gdansk', 'Szczecin']

def start():
    for city in CITIES:
        try:
            logger.info('Starting pipline')
            weather_df = extract_weather(city)
            
            logger.info('Transforming data')
            weather_df = transform_weather(weather_df, city)

            logger.info('Loading data')
            load(weather_df, 'weather')

            logger.info('ETL pipline done')

        except:
            logger.exception('Pipline failed')
            print('Pipline Failed')
            raise

if __name__ == '__main__':
    start()