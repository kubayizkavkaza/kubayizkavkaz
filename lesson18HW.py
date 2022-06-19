import api_temp
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(16, 10))

d_cities_new = api_temp.get_cities_temp()

axes = figure.add_subplot(2, 2, 1)  # строка, столбец, индекс графика

cities_new = d_cities_new.keys()
temper = d_cities_new.values()

# create the barchart
axes.bar(cities_new, temper)
axes.set_title('Температура в разных городах')
axes.set_ylabel('Значение температуры')
axes.set_xlabel('Город')

timeeee, temppp, feeels_like = api_temp.get_forecast()

axes2 = figure.add_subplot(2, 2, 2)
plt.plot(timeeee, temppp, label="Температура")
plt.plot(timeeee, feeels_like, label="Ощущается как")

plt.xticks(timeeee[::3], rotation=18, ha='right')
plt.title('Прогноз погоды в Москве за 5 дней')
plt.xlabel("t прогноза погоды за 5 дней каждые 9ч")
plt.ylabel('Значение температуры/ощущается как')
plt.legend()
plt.grid()


m = api_temp.get_forecast_cities_temp()

axes3 = figure.add_subplot(2, 2, 3)
for s_city in m:
    x, y = m[s_city]
    plt.plot(x, y, label=s_city)
    plt.xticks(x[::3], rotation=18, ha='right')
plt.title('Прогноз temp в разных городах')
plt.ylabel('Значение temp')
plt.xlabel('Дата/Время')
plt.legend()
plt.grid()

k = api_temp.get_forecast_cities_feels_like()

axes4 = figure.add_subplot(2, 2, 4)
for s_city in k:
    x, y = k[s_city]
    plt.plot(x, y, label=s_city)
    plt.xticks(x[::3], rotation=18, ha='right')
plt.title('Прогноз feels_like в разных городах')
plt.ylabel('Значение feels_like')
plt.xlabel('Дата/Время')
plt.legend()
plt.grid()

plt.show()

# TODO clean the code in api_temp.py and how to optimize it
# TODO разобрать и сделать принты данных (sys clounds wind and etc. )которые возвращаются в json - data