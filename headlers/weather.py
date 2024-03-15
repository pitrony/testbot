from aiogram import types, F, Router
from aiogram.filters.command import Command
import requests
from utilits import weath
from aiogram.filters.command import Command
#from aiogram.fsm.context import FSMContext
#from aiogram.fsm.state import State, StatesGroup
from keyboard.prof_keyboards import make_row_keyboard

weather_names = ['Погода в СПб', 'Погода в Москве', 'Инфо']


router = Router()
#class ChoiseProfName(StatesGroup):
#   choise_city_name = State()
#   переменная для выбора города

@router.message(Command('weather'))
async def mes_weather(message: types.Message):
  #  name = message.chat.first_name
    temp = weath.weathers()
    city = weath.weathers()
    await message.answer(f'Погода нынче в городе {city} такая {temp}', reply_markup=make_row_keyboard(weather_names))
@router.message(F.text.lower() == 'погода')
async def cmd_weather(message: types.Message):
  #  name = message.chat.first_name
    await message.answer(f'Now weather is cold')
