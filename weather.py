import logging
import os
import requests

my_api_key = '49f7e955640dc6bd40306613fb18e0d0'

class WeatherToday():
    def __init__(self, *args):
        self.api_key = args 
    
    def city_request(self, api_key):
        city = input('Enter city/region/airport name: ')
        data = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}').json()
        if data != []:
            print('Please, choose the city: ')
            i = 1
            for city in data:
                print(f" Press {i} if {city['name']}, {city['country']}")
                i+=1  
        else:
            logging.warning("Cant find city/region/airport with such name, please try again")
            raise SystemExit#error
        while True:
            try:
                print("If you want to quit press Y")
                choice = input('Enter Number: ')
                if choice =='Y':
                    raise SystemExit
                else:
                    choice = int(choice)
                    break
            except ValueError:
                logging.warning("That was not a number. Try again")          
        return data, choice    
                   
    def weather_today(self, api_key):
        data, choice = self.city_request(api_key)
        try:
            if choice > 0 and choice < len(data):
                weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={data[choice - 1]['name']},{data[choice -1]['country']}&appid={api_key}&units=metric").json()
                os.system('cls||clear')
                print(f"Temperature in {data[choice - 1]['name'], data[choice -1]['country']} is {weather['main']['temp']} \u2103")
            else:
                logging.warning("You chose incorrect number")
        except KeyError:
            logging.warning("Cant find city/region/airport with such name, please try again")
        
if __name__ == '__main__':
    weather = WeatherToday(my_api_key)      
    weather.weather_today(my_api_key)

