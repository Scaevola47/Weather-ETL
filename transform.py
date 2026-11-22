import pandas as pd

def transform_weather(weather):
    df = weather.copy()

    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['datetime'])
    df = df[[
            'datetime', 'temp', 'windspeed', 'humidity', 'pressure', 'conditions'
        ]]

    return df
