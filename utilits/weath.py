import requests
import asyncio
import json
import config
def weathers():
    weather_key = config.weather_key
    #id: 14,cityid: '498817',appid: 'cfcfe73689ce00355c0d2a157b211d4c',units: 'metric'
    #url = 'http://api.openweathermap.org/data/2.5/weather?q=Moskow&APPID={weather_key}'
    #http://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&APPID=cfcfe73689ce00355c0d2a157b211d4c
    url = 'https://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&callback=test&appid={weather_key}'
    response = requests.get(url)

    if response.status_code:
        data = response.json()
        #description = data['weather'][0]['description']
        #['main]['humidity]
        #city=data['name']
        #pressure = data['main']['pressure']
        #wind = data['wind']['speed']
        #return (cur_temp)

        temp = int(data["main"]["temp"] - 273.15)  # convert from Kelvin to Celsius
       # return temp
    else:
        temp=0
    return temp

if __name__ == '__main__':
        weathers()
 #async def get_weather(city: str) -> str:
  #  response = requests.get(f"appid=YOUR_OPENWEATHERMAP_API_KEY")
   # data = response.json()
    #description = data['weather'][0]['description']
    #temp = int(data['main']['temp'] - 273.15)  # convert from Kelvin to Celsius
    #return f"Weather in {city}: {description}, temperature: {temp}°C"
#@router.message(Command('weather'))
 #async def weather(message: types.Message):
  #  city = message.text.split('/weather', 1)[1].strip()
   # await message.reply(await get_weather(city))