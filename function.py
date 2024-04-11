import os
import requests
import json

class WeatherWrapper:
    def __init__(self):
        self.api_key = '303cc60b4908b33b88f1dfa22fc51ed9'
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self, lat, lon):
        print(self.base_url)
        complete_url = self.base_url +"lat=" + str(lat)+  "&lon=" + str(lon)+"&appid=" + self.api_key
        response = requests.get(complete_url)
        data = response.json()
        return data


if __name__ == "__main__":
    latitude = float(os.environ.get("LAT", 0.0))
    longitude = float(os.environ.get("LONG", 0.0))
    weather_wrapper = WeatherWrapper()
    weather_info = weather_wrapper.get_weather(latitude, longitude)
    print(weather_info)
