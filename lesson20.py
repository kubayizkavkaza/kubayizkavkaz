from tkinter import *

import matplotlib

import api_temp

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

city_name = ''


def show_message():
    global city_name
    city_name = message.get()
    # create a figure
    figure = Figure(figsize=(15, 10), dpi=100)

    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure)

    d_cities_new = api_temp.get_cities_temp()

    axes = figure.add_subplot(2, 2, 1)  # строка, столбец, индекс графика

    cities_new = d_cities_new.keys()
    temper = d_cities_new.values()

    # create the barchart
    axes.bar(cities_new, temper)
    axes.set_title('Температура в разных городах')
    axes.set_ylabel('Значение температуры')
    axes.set_xlabel('Город')

    city_times, city_temps, city_feeeels_like = api_temp.get_forecast(city_name)

    axes2 = figure.add_subplot(2, 2, 2)
    axes2.plot(city_times, city_temps, label="Температура")
    axes2.plot(city_times, city_feeeels_like, label="Ощущается как")

    axes2.set_xticks(city_times[::3], rotation=18, ha='right')
    axes2.tick_params(axis='x', rotation=18)
    axes2.set_title(f'Прогноз погоды в {city_name} за 5 дней')
    axes2.set_xlabel("t прогноза погоды за 5 дней каждые 9ч")
    axes2.set_ylabel('Значение температуры/ощущается как')
    axes2.legend()
    axes2.grid()
    try:
        api_temp.print_city_info(city_name)
    except:
        print('Уровня моря и земли в этом городе нет')

    figure_canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    city_times2, valuee = api_temp.get_forecast_city_temp(city_name)

    axes3 = figure.add_subplot(2, 2, 3)

    axes3.plot(city_times2, valuee, label=f'Температура в {city_name}')
    axes3.set_xticks(city_times2[::3], rotation=18, ha='right')
    axes3.tick_params(axis='x', rotation=18)
    axes3.set_title(f'Прогноз temp в {city_name}')
    axes3.set_ylabel('Значение temp')
    axes3.set_xlabel('Дата/Время')
    axes3.legend()
    axes3.grid()

    city_times1, valuess = api_temp.get_forecast_city_feels_like(city_name)

    axes4 = figure.add_subplot(2, 2, 4)
    axes4.plot(city_times1, valuess, label=f'"Ощущается как" в {city_name}')
    axes4.set_xticks(city_times1[::3], rotation=18, ha='right')
    axes4.tick_params(axis='x', rotation=18)
    axes4.set_title(f'Прогноз "Ощущается как" в {city_name}')
    axes4.set_ylabel('Значение "Ощущается как"')
    axes4.set_xlabel('Дата/Время')
    axes4.legend()
    axes4.grid()


root = Tk()
root.title("GUI на Python")
root.geometry("1500x800")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="center")

message_button = Button(text="Click Me", command=show_message)
message_button.place(relx=.5, rely=.5, anchor="center")

root.mainloop()

print(city_name)
