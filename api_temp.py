from datetime import datetime

import requests  # cmd --> pip install requests

appid = 'a54dae422193d293bce4233256f0002f'


def get_city_id(s_city):
    res = requests.get("http://api.openweathermap.org/data/2.5/find", params={
        'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid
    })
    data = res.json()
    city_id = data['list'][0]['id']
    return city_id


def get_city_weather_details(s_city):
    city_id = get_city_id(s_city)
    res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={
        'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid
    })
    return res.json()


def get_city_forecast_details(s_city='Moscow,RU'):
    city_id = get_city_id(s_city)
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    return res.json()


def get_cities_temp(s_cities=("London,GB", "Moscow,RU", "Kiev,UA", "Petersburg", "Volgograd, RU")):
    d_cities = {}
    for s_city in s_cities:
        data = get_city_weather_details(s_city)
        d_cities[s_city] = data['main']['temp']
    return d_cities


def get_forecast(s_city='Moscow,RU'):
    data = get_city_forecast_details(s_city)
    times = []
    forecast_temp = []
    forecast_feels_like = []
    for i in data['list']:
        times.append(i['dt_txt'][:-3])
        forecast_temp.append(i['main']['temp'])
        forecast_feels_like.append(i['main']['feels_like'])
    return times, forecast_temp, forecast_feels_like


def get_forecast_city_temp(s_city='Moscow,RU'):
    times, forecast_temp, _ = get_forecast(s_city)
    return times, forecast_temp


def get_forecast_city_feels_like(s_city='Moscow,RU'):
    times, _, forecast_feels_like = get_forecast(s_city)
    return times, forecast_feels_like


def get_forecast_cities_temp(s_cities=("London,GB", "Moscow,RU", "Kiev,UA", "Petersburg", "Volgograd, RU")):
    d_cities = {}
    for s_city in s_cities:
        d_cities[s_city] = get_forecast_city_temp(s_city)
    return d_cities


def get_forecast_cities_feels_like(s_cities=("London,GB", "Moscow,RU", "Kiev,UA", "Petersburg", "Volgograd, RU")):
    d_cities = {}
    for s_city in s_cities:
        d_cities[s_city] = get_forecast_city_feels_like(s_city)
    return d_cities

def print_city_info(s_city = 'Moscow,RU'):
    res = requests.get("http://api.openweathermap.org/data/2.5/find", params={
        'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid
    })
    data = res.json()
    city_id = data['list'][0]['id']
    res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={
        'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid
    })
    city_id = data['list'][0]['id']
    print(f'ID ???????????? {s_city}: {city_id}')
    city_name = data['list'][0]['name']
    print(f'???????????????? ????????????: {city_name}')
    print(f"???????????????????? ???????????? {s_city}: ")
    city_coord_lat = data['list'][0]['coord']['lat']
    print(f'\t????????????: {city_coord_lat}')
    city_coord_lon = data['list'][0]['coord']['lon']
    print(f'\t??????????????: {city_coord_lon}')
    city_temp = data['list'][0]['main']['temp']
    print(f'?????????????????????? ?? {s_city}: {city_temp}???')
    city_feels_like = data['list'][0]['main']['feels_like']
    print(f'"?????????????????? ??????" ?? {s_city}: {city_feels_like}???')
    city_mintemp = data['list'][0]['main']['temp_min']
    print(f'?????????????????????? ?????????????????????? ?? {s_city}: {city_mintemp}???')
    city_maxtemp = data['list'][0]['main']['temp_max']
    print(f'???????????????????????? ?????????????????????? ?? {s_city}: {city_maxtemp}???')
    city_pressure = data['list'][0]['main']['pressure']
    print(f'???????????????? ?? {s_city}: {city_pressure}??????')
    city_humidity = data['list'][0]['main']['humidity']
    print(f'?????????????????? ?? {s_city}: {city_humidity}%')
    city_timestamp = data['list'][0]['dt']

    print(datetime.utcfromtimestamp(city_timestamp).strftime('?????????? ????????????(UTC): %Y-%m-%d %H:%M:%S'))
    print(datetime.utcfromtimestamp(city_timestamp).strftime('???????? ????????????(UTC): %Y-%m-%d'))
    city_speedwind = data['list'][0]['wind']['speed']
    print(f'???????????????? ?????????? ?? {s_city}: {city_speedwind} ??/??')
    city_checkrain = data['list'][0]['rain']
    if city_checkrain is None:
        print(f'?????????? ?? {s_city} ???? ????????')
    else:
        print(f'?????????? ?? {s_city} ????????')
    city_checksnow = data['list'][0]['snow']
    if city_checksnow is None:
        print(f'???????? ?? {s_city} ???? ????????')
    else:
        print(f'???????? ?? {s_city} ????????')
    city_clouds = data['list'][0]['clouds']['all']
    print(f'???????????????????? ?? {s_city}: {city_clouds}%')
    # city_weather = data['list'][0]['weather']
    # print(f'???????????? ?? {s_city}: {city_weather}')
    city_numicon = data['list'][0]['weather'][0]['icon']

    print(f'?????????????????????? ???????????? ?? {s_city} ????????????????: https://openweathermap.org/img/wn/{city_numicon}@4x.png')
    city_shortdesc = data['list'][0]['weather'][0]['description']
    print(f'?????????????????? ???????????????? ???????????? ?? {s_city}: {city_shortdesc}')
    city_sealevel = data['list'][0]['main']['sea_level']
    print(f'?????????????? ???????? ?? {s_city}: {city_sealevel} ????')
    city_grndlevel = data['list'][0]['main']['grnd_level']
    print(f'?????????????? ??????????/???????????? ?? {s_city}: {city_grndlevel} ????')