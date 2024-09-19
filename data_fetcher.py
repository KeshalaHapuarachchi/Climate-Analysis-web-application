import requests

API_KEY = '3515184e36318f46647fa41aadeb0805'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def fetch_climate_data(city):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(complete_url)
    return response.json()
