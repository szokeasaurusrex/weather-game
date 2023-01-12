import requests
import random

# Dictionary here
city = {
    "New York": (40.7127837, -74.0059413),
    "Los Angeles" : (34.0522342, -118.2436849),
    "Chicago" : (41.8781136, -87.6297982),
    "Tokyo" : (35.6839, 139.7744),
    "Mexico City" : (19.4333, -99.1333),
    "Mumbai" : (18.9667, 72.8333),
    "São Paulo" : (-23.5504, -46.6339),
    "Beijing" : (39.9042, 116.4074),
    "London" : (51.5072, 0.1276),
    "Seoul" : (37.5665, 126.9780),
    "Cario" : (30.0444, 31.2357),
    "Paris" : (48.8566, 2.3522),
    "Shanghai" : (31.2304, 121.4737),
    "Istanbul" : (-41.0082, -28.9784),
    "Buenos Aires" : (34.6037, 58.3816),
    "Budapest": (47.4979, 19.0402),
    "Vienna": (48.2082, 16.3738),
    "Cleveland": (41.4993, -81.6944),
    "Istanbul" : (41.0082, 28.9784),
    "Buenos Aires" : (34.6037, 58.3816),
    "Berlin" : (52.5200, 13.4050),
    "Hong Kong" : (22.3193, 114.1694),
    "Washington DC" : (38.9072, -77.0369)
}

def weather_summary(conditions):
    weather_codes = {
        0: "clear",
        1: "mainly clear",
        2: 'partly cloudy',
        3: 'overcast',
        45: 'fog',
        48: 'depositing rime fog',
        51: 'light drizzle',
        53: 'moderate drizzle',
        55: 'dense drizzle',
        56: 'light freezing drizzle',
        57: 'dense freezing drizzle',
        61: 'slight rain',
        63: 'moderate rain',
        65: 'heavy intensity',
        66: 'light freezing rain',
        67: 'heavy freezing rain',
        71: 'slight snow fall',
        73: 'moderate snow fall',
        75: 'heavy snow fall',
        77: 'snow grains',
        80: 'slight rain showers',
        81: 'moderate rain showers',
        82: 'violent rain showers',
        85: 'slight snow showers',
        86: 'heavy snow showers',
        95: 'thunderstorm',
        96: 'thunderstorm with slight hail',
        99: 'thunderstorm with heavy hail'
    }
    temp = conditions['temperature']
    condition_string = weather_codes[conditions['weathercode']]
    return f'Temperature (C): {temp}; Conditions: {condition_string}'



# API here
city_guesses = random.sample(list(city), 4)
correct = city_guesses[random.randint(0, 3)]

latitude = city[correct][0]
longitude = city[correct][1]
response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
print(f'Guess which city had this weather:\n{weather_summary(response.json()["current_weather"])}\n')

for i, guess in enumerate(city_guesses):
    print(f'{i}: {guess}')

input()

print(f'The correct answer was {correct}.')