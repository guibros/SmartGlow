"""
Ce fichier contient la classe qui obtient la météo.
Il a des méthodes pour obtenir la météo actuelle
ainsi que les prévisions météorologiques.
"""


from datetime import datetime as dt
from urllib.request import urlopen
import requests
import io


#################
# WEATHER SETUP #
#################

# WEATHER SETUP
class Weather:
    def __init__(self):
        self.temperature = ''
        self.feels = ''
        self.mini = ''
        self.maxi = ''
        self.humi = ''
        self.icon = ''
        self.bigW = ''
        self.all = ''
        self.forecast = ''
        
    def getWeather(self):
        api_key = "5b4170c6920b99f9871cacd31213823e"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + 'Montreal'
        response = requests.get(complete_url)
        x = response.json()
        self.all = x['main']
        self.temperature = "Current temperature: " + str(int(float(x['main']['temp']-273.15))) + " C"
        self.bigW = str(int(float(x['main']['temp']-273.15)))
        self.feels = str(int(float(x['main']['feels_like']-273.15)))
        self.mini = str(int(float(x['main']['temp_min']-273.15)))
        self.maxi = str(int(float(x['main']['temp_max']-273.15)))
        self.humi = str(x['main']['humidity'])

    def getForecast(self):
        api_key = "5b4170c6920b99f9871cacd31213823e"
        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
        complete_url = base_url + "appid=" + api_key + "&q=" + 'Montreal'
        response = requests.get(complete_url)
        x = response.json()
        self.forecast = []
        for day in x['list']:
            time = day['dt_txt'][11:] 
            if time == '12:00:00':
                date = day['dt_txt'][:10] 
                self.bigW = str(int(float(day['main']['temp']-273.15)))
                self.feels = str(int(float(day['main']['feels_like']-273.15)))
                self.mini = str(int(float(day['main']['temp_min']-273.15)))
                self.maxi = str(int(float(day['main']['temp_max']-273.15)))
                self.forecast.append((date, self.bigW))
            
    
    def currentForecast(self):
        self.getForecast()
        return [f"Demain, le {self.forecast[0][0][-2:]}, il fera {self.forecast[0][1]} degré Celsius, le {self.forecast[1][0][-2:]}, il fera {self.forecast[1][1]} degré et le {self.forecast[2][0][-2:]}, il fera {self.forecast[2][1]}",
                f"{self.forecast[0][0]} : {self.forecast[0][1]} C\n\n{self.forecast[1][0]} : {self.forecast[1][1]} C\n\n{self.forecast[2][0]} : {self.forecast[2][1]} C"]
        
    def currentWeather(self):
        self.getWeather()
        return [f"La température éxtérieure est présentement {self.bigW} degré celsius.\
            La température ressentie est de {self.feels} degré. Le minimum est de {self.mini}\
            avec un maximum de {self.maxi}. Il y a un taux d'humidité de {self.humi}.",
            f"Éxtérieure: {self.bigW} C        Ressentie: {self.feels} C\nMinimum: {self.mini} C        Maximum: {self.maxi} C\nHumidité: {self.humi}"]
        
        

if __name__ == '__main__':
    temp = Weather()
    print(temp.currentForecast())
    print(temp.currentWeather())