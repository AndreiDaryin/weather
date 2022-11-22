import logging
import os

import requests

my_api_key = '49f7e955640dc6bd40306613fb18e0d0'

class WeatherToday():
    def __init__(self, *args):
        self.api_key = args
    
    def city_choice(self):    
        try:
            choice = int(input('Enter Number: '))
        except ValueError:
            logging.warning("That was not a number. Try again")
            self.city_choice()
        return choice    
    
    def city_request(self, api_key):
        city = input('Enter city/region/airport name: ')
        data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}').json()
        if data != []:
            print('Please, choose the city: ')
            for i in range(len(data)):
                print(f" Number {i} {data[i]['name']}, {data[i]['country']}")
        choice = self.city_choice()
        return data, choice      
                   
    def weather_today(self, api_key):
        data, choice = self.city_request(api_key)
        try:
            weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={data[choice]['name']},{data[choice]['country']}&appid={api_key}&units=metric").json()
            os.system('cls||clear')
            print(f"Temperature in {data[choice]['name'], data[choice]['country']} is {weather['main']['temp']} \u2103")
        except KeyError:
            logging.warning("Cant find city/region/airport with such name, please try again")
        
if __name__ == '__main__':
    weather = WeatherToday(my_api_key)      
    weather.weather_today(my_api_key)

