from sqlalchemy import create_engine
import pandas as pd
from extract import extract_weather
from load import load
from transform import transform_weather

def start():
    try:
        print('Starting pipline')

        weather_df = extract_weather()
        print('Starting transformation')

        weather_df = transform_weather(weather_df)
        load(weather_df, 'weather')

        print('ETL pipline done')

    except:
        print('Pipline Failed')

if __name__ == '__main__':
    start()