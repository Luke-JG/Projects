import requests
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

API_KEY = '91accaddcd2ca409e9c283b294a8957b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
    }
    try:
        response = requests.get(BASE_URL + 'weather', params=params)
        data = response.json()

        weather_description = data['weather'][0]['description'].capitalize()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        icon_code = data['weather'][0]['icon']

        return weather_description, temperature, humidity, icon_code
    except requests.exceptions.RequestException as e:
        return None, None, None, None

def update_weather():
    city = city_entry.get()
    weather_description, temperature, humidity, icon_code = get_weather(city)

    if weather_description:
        status_label.config(text=f'Weather in {city}: {weather_description}')
        temp_label.config(text=f'Temperature: {temperature}°C')
        humidity_label.config(text=f'Humidity: {humidity}%')

        # Load and display weather icon from OpenWeatherMap
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}.png'
        icon_response = requests.get(icon_url, stream=True)
        if icon_response.status_code == 200:
            icon_data = icon_response.content
            icon = PhotoImage(data=icon_data)
            icon_label.config(image=icon)
            icon_label.image = icon

        # Display animations based on weather description
        display_animation(weather_description)

    else:
        status_label.config(text='Error: Unable to fetch weather data.')

def display_animation(weather_description):
    if 'rain' in weather_description.lower():
        animation = PhotoImage(file='rain_animation.gif')
    elif 'sunny' in weather_description.lower():
        animation = PhotoImage(file='sunny_animation.gif')
    else:
        # Default animation for other weather conditions
        animation = PhotoImage(file='default_animation.gif')

    animation_label.config(image=animation)
    animation_label.image = animation

# Create the GUI window
root = tk.Tk()
root.title('Weather App')

# Modern styling
root.geometry('400x500')
root.configure(bg='#000000')

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

font_style = ('Arial', 14, 'bold')
label_fg_color = '#FFFFFF'

city_label = ttk.Label(frame, text='Enter a city:', font=font_style, foreground=label_fg_color, background='#000000')
city_label.grid(row=0, column=0, sticky='w')

city_entry = ttk.Entry(frame, width=20, font=font_style)
city_entry.grid(row=0, column=1, sticky='w')

search_button = ttk.Button(frame, text='Search', command=update_weather, style='TButton')
search_button.grid(row=0, column=2, sticky='w')

status_label = ttk.Label(frame, text='', font=font_style, foreground=label_fg_color, background='#000000')
status_label.grid(row=1, columnspan=3, pady=(10, 0))

temp_label = ttk.Label(frame, text='', font=font_style, foreground=label_fg_color, background='#000000')
temp_label.grid(row=2, columnspan=3)

humidity_label = ttk.Label(frame, text='', font=font_style, foreground=label_fg_color, background='#000000')
humidity_label.grid(row=3, columnspan=3)

icon_label = ttk.Label(frame)
icon_label.grid(row=2, column=3, rowspan=2)

animation_label = ttk.Label(frame)
animation_label.grid(row=4, columnspan=4, pady=(10, 0))

style = ttk.Style()
style.configure('TButton', font=font_style, foreground='#FFFFFF', background='#007acc')

root.mainloop()
