import os
import requests

my_api_key = '49f7e955640dc6bd40306613fb18e0d0'

class WeatherToday():
    def __init__(self, *args):
        self.api_key = args
    
    def weather_today(self, api_key):
        city = input('Enter city/region/airport name: ')
        data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}').json()
        try:
            if data != []:
                print('Please, choose the city: ')
                for i in range(len(data)):
                    print(f" Number {i} {data[i]['name']}, {data[i]['country']}")
                try:
                    choice = int(input('Enter Number: '))
                except ValueError:
                    print("That was not a number. Try again")
                    choice = int(input('Enter Number: '))
                weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={data[choice]['name']},{data[choice]['country']}&appid={api_key}&units=metric").json()
                os.system('cls||clear')
                print(f"Temperature in {data[choice]['name'], data[i]['country']} is {weather['main']['temp']} \u2103")
            else:
                print('Cant find city/region/airport with such name, please try again')
        except KeyError:
            print('Cant find city/region/airport with such name, please try again')
        
weather = WeatherToday(my_api_key)      
weather.weather_today(my_api_key)

