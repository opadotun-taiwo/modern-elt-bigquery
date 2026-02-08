import requests


api_key = '12aa5189fd8ae297f1335107b1c75923'
api_url = f'https://api.weatherstack.com/current?access_key={api_key}&query=Los Angeles,Chicago,California,Phoenix,Philadelphia,San Antonio,San Diego'

def fetch_data():
    print('Started fetching data from weatherstack...')
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print('Api responded successfully')
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        print('An error occured {e}')
        raise

#fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-12-10 20:58', 'localtime_epoch': 1765400280, 'utc_offset': '-5.0'}, 'current': {'observation_time': '01:58 AM', 'temperature': 5, 'weather_code': 122, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Overcast'], 'astro': {'sunrise': '07:09 AM', 'sunset': '04:28 PM', 'moonrise': '11:01 PM', 'moonset': '11:42 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 69}, 'air_quality': {'co': '295.85', 'no2': '38.05', 'o3': '23', 'so2': '10.15', 'pm2_5': '20.45', 'pm10': '20.55', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 26, 'wind_degree': 219, 'wind_dir': 'SW', 'pressure': 997, 'precip': 1.1, 'humidity': 79, 'cloudcover': 100, 'feelslike': 0, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}

