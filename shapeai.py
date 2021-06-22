import requests

from datetime import datetime

api_key = "1896957cd18c4348fa233f074bb2fab3"
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %m %Y | %H:%M:%S ")


L = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
m = "Current temperature is: {:.2f} deg C".format(temp_city)
n =  "Current weather desc  :", weather_desc
o = " Current Humidity      :", hmdt, '%'
p = "Current wind speed    :", wind_spd ,'kmph'
d = [L,m,n,o,p]

file_dis = input("enter file name to display the content")
fd = open(file_dis,"x")
for i in range(len(d)):
    fd.write(str(d[i]))
    fd.write("\n")

fd.close()

