import requests
from datetime import datetime
from pprint import pprint

API_KEY = 'LexF14OpozJ6ufGfrqk1w2PjWEm58ALj'
LAT = 33.0089
LON = 35.0945

# === get locationKey ===
location_url = 'https://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
params = {
    'apikey': API_KEY,
    'q': f'{LAT},{LON}'
}

response = requests.get(location_url, params=params)
data = response.json()
location_key = data['Key']
print(f"🔑 Location Key: {location_key}")

# # === get a 12-hour forecast ===
forecast_url = f'https://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}'
params = {
    'apikey': API_KEY,
    'language': 'en-us',
    'metric': 'true'
}

response = requests.get(forecast_url, params=params)
forecast_data = response.json()
# pprint(forecast_data)

print("\n📅 12-hour forecast:")
for hour in forecast_data:
     dt = datetime.strptime(hour['DateTime'], '%Y-%m-%dT%H:%M:%S%z')
     time_str = dt.strftime('%H:%M')
     temp = hour['Temperature']['Value']
     phrase = hour['IconPhrase']
     print(f"{time_str}, {temp}°C, {phrase}")

# output:
# 12:00, 21.7°C, Cloudy
# 13:00, 21.1°C, Cloudy
# 14:00, 20.8°C, Cloudy
# 15:00, 20.3°C, Cloudy
# 16:00, 20.3°C, Cloudy
# 17:00, 20.1°C, Cloudy
# 18:00, 19.7°C, Cloudy
# 19:00, 19.7°C, Cloudy
# 20:00, 19.1°C, Cloudy
# 21:00, 19.1°C, Cloudy
# 22:00, 19.0°C, Cloudy
# 23:00, 18.3°C, Mostly cloudy