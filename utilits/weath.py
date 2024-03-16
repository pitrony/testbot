import requests
import asyncio
import gson
import config
def weathers():
    weather_key = config.weather_key

    url = 'https://api.openweathermap.org/data/2.5/weather?q=москва&lang=ru&units=metric&appid={weather_key}'
    response = requests.get(url)

    if response.status_code:
        wdata = response.json()
        #description = data['weather'][0]['description']
        #['main]['humidity]
        city = wdata.get('name', {})
        #pressure = data['main']['pressure']
        #wind = data['wind']['speed']
        #return (cur_temp)
        #idweather=data['weather']['id']
        #temp=wdata.get('weather', {}).get('id')
        temp = wdata.get('main', {}).get('temp')   #  Celsius
       # return temp
      #  async def cmd_weath_ans(message: types.Message):
      # await message.answer(f'Weather , {temp}')
    else:
        temp="null"
    return (temp, city)

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