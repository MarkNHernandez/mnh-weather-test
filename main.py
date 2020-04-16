import sqlite3
import requests

#connect to the database and assign the cursor object
conn = sqlite3.connect('/Volumes/XStorage/MNH/Weather_Data/weather.sqlite3')
c = conn.cursor()

def getDate(dati):
    date = dati[0:10]
    return date

def getTime(dati):
    time = dati[11:19]
    return time

def Cel2Fahr(temp):
    fahr = (temp * (9/5) + 32)
    return round(fahr,2)

#assign the location variable
location = "Chicago"

url = "http://metaweather.com/api/location/2379574"

#created by Postman
payload = {}
headers = {}

#send the request to the server and assign the response to a variable
response = requests.get(url)

#assign the temperature response to to temp
temp = response.json()["consolidated_weather"][0]['the_temp']

#assign the DAte and TIme to DATI
dati = response.json()["time"]

#print(location)
Date = (getDate(dati))
Time = (getTime(dati))
TempC = (round(temp,2))
TempF = (Cel2Fahr(temp))
print(round(temp,2))
package = (location, Date, Time, TempC, TempF)
sql = "INSERT INTO temperature VALUES ('{}', '{}', '{}', '{}', '{}');".format(*package)
print(sql)
c.execute(sql)
conn.commit()
conn.close()
