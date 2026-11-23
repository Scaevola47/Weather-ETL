import pandas as pd
import requests
import logging

BASE_CITY = 'Slupsk'
BASE_URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{BASE_CITY},PL?unitGroup=metric'

def city_url(city):
    return f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city},PL?unitGroup=metric'

logger = logging.getLogger(__name__)
def extract_weather(city = BASE_CITY):
    try:
        logger.info(f'Extracting info for {city}')
        url = city_url(city)
        #url = f'{BASE_URL}'
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        rows = []
        for day in data["days"]:
            for hour in day.get("hours", []):   
                hour["date"] = day["datetime"]
                rows.append(hour)

        return pd.DataFrame(rows)
    except:
        logger.exception(f'Error while extracting for {city}')
        raise


