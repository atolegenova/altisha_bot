import requests
import json


weather_api = '5694bdbf0dbf4cabd17ad54be52e6594'
weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=Bishkek&appid='+ weather_api

#w = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q=Bishkek&appid={weather_api}').json()
def get_weather():
    response = requests.get(weather_url)
    data = json.loads(response.content)
    # for elem in data['weather']:
    #     weather_state = elem['main']
    #     print(weather_state)
    temp_min = round(data['main']['temp_min'] - 273.15, 1)
    temp_max = round(data['main']['temp_max'] - 273.15, 1)
    #city = data['name']
    print(data)
    msg = f'Погода в Бишкеке на сегодня:  Температура от {temp_min} до {temp_max} градусов Целсия '

    return msg

weather = get_weather()

