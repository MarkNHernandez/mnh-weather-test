import sqlite3
import requests

def Cel2Fahr(temp):
    fahr = (temp * (9/5) + 32)
    return round(fahr,2)

url = "http://metaweather.com/api/location/2379574"

payload = {}
headers = {}

response = requests.get(url, params=payload)
temp = response.json()["consolidated_weather"][0]['the_temp']
print(Cel2Fahr(temp))

#conn = sqlite3.connect('weather.db')


#c = conn.cursor()

