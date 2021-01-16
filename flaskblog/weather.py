import requests, json
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "cd0c3ecb0b73431373fe3c3a36caffb1"

URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY



def weather_data(CITY):
    city=CITY
    response = requests.get(URL)
    if response.status_code == 200:\
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        return [CITY,temperature,humidity,pressure,report]
    else:
    print("Error in the HTTP request")