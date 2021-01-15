# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = 'iit'
API_KEY = "cd0c3ecb0b73431373fe3c3a36caffb1"
# upadting the URL
try:
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
        report = data['weather']
        print(CITY + " weather")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
    # showing the error message
        print("Error in the HTTP request")
except:
    print('error')