import requests

api_key = "c0e5b9bbfc8069b5346932f637dfbed9"
api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error accured: {e}")
        raise

# fetch_data()

def mock_fetch_data():
    return {
            'request': {
                'type': 'City',
                'query': 'New York, United States of America',
                'language': 'en',
                'unit': 'm'
            },
            'location': {
                'name': 'New York',
                'country': 'United States of America',
                'region': 'New York',
                'lat': '40.714',
                'lon': '-74.006',
                'timezone_id': 'America/New_York',
                'localtime': '2025-12-22 23:16',
                'localtime_epoch': 1766445360,
                'utc_offset': '-5.0'
            },
            'current': {
                'observation_time': '04:16 AM',
                'temperature': 3,
                'weather_code': 113,
                'weather_icons': [
                    'https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'
                ],
                'weather_descriptions': ['Clear'],
                'wind_speed': 14,
                'wind_degree': 244,
                'wind_dir': 'WSW',
                'pressure': 1030,
                'precip': 0,
                'humidity': 44,
                'cloudcover': 25,
                'feelslike': -1,
                'uv_index': 0,
                'visibility': 16,
                'is_day': 'no'
            }
        }