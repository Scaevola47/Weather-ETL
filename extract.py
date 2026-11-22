import pandas as pd
import requests

city_url = 'Slupsk'
BASE_URL = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city_url},PL?unitGroup=metric'

def extract_weather():
    url = f'{BASE_URL}'
    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    rows = []
    for day in data["days"]:
        for hour in day.get("hours", []):   
            hour["date"] = day["datetime"]
            rows.append(hour)

    return pd.DataFrame(rows)


