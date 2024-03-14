import requests
#import config
def weather():
    weather_ky = config.weather_key
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Moskow&appid={weather_ky}'
    response = requests.get(url)

    if response.status_code:
        data = response.json()
        return data.get('main.temp')

if __name__ == '__main__':
        weather()
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