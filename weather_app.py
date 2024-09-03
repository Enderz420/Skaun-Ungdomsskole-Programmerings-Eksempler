import requests
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('WEATHER_API_KEY')

api_key = SECRET_KEY
city = input('Insert City Name\n')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)


while True:    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        
        print(f'Temperature: {temp} K')
        
        tempCelcius = temp - 273.15
        round(tempCelcius)
        
        print(f'Temperature in Celcius: {tempCelcius}C')
        print(f'Description: {desc}')
        
        exit = input("type "'something'"to quit")
        if exit.isalpha():
            break
    else:
        print('Error fetching weather data')
        break