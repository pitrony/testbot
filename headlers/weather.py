from aiogram import types, F, Router
from aiogram.filters.command import Command
import requests
#import os
from utilits import weath
import config
from aiogram.filters.command import Command
#from aiogram.fsm.context import FSMContextgit status
#from aiogram.fsm.state import State, StatesGroup
from keyboard.prof_keyboards import make_row_keyboard

weather_names = ['Погода в СПб', 'Погода в Москве', 'Инфо']
weather_key = config.weather_key

router = Router()
#class ChoiseProfName(StatesGroup):
#   choise_city_name = State()
#   переменная для выбора города

@router.message(Command('weather'))
async def mes_weather(message: types.Message):
   #  name = message.chat.first_name
   # temp, city = weath.weathers()
   await message.answer(f'Чтоб узнать погоду, выберите нужный город', reply_markup=make_row_keyboard(weather_names))
   #await message.answer(f'Погода нынче в городе {city} такая {temp}', reply_markup=make_row_keyboard(weather_names))
@router.message(F.text.lower() == 'погода в спб')
async def cmd_weather_spb(message: types.Message):
  #  name = message.chat.first_name
  city = str('Санкт-Петербург')
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={weather_key}"
  res = requests.get(url)
  data = res.json()
  temp = data.get('main',{}).get('temp')
  #temp = str(data["main"]["temp"])
  #res = requests.get(url)
  #data = res.json().get("main")
  #weather1 = str(temp)
  await message.answer(f'В городе {city} {temp} градусов по цельсия')
  #await message.answer(message.from_user.id, f'В городе *{city}* {weather1} градусов по цельсия',
                         #parse_mode="Markdown")

@router.message(F.text.lower() == 'погода в москве')
async def cmd_weather_msk(message: types.Message):
  city = str("Москва")
  url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={weather_key}"
  res = requests.get(url)
  data = res.json()
  temp = data['main']['temp']
  weather1 = str(temp)
  await message.answer(f'В городе {city} {weather1} градусов по цельсия')