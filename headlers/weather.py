from aiogram import types, F, Router
import requests
from utilits import weath
from aiogram.filters.command import Command
#from aiogram.fsm.context import FSMContext
#from aiogram.fsm.state import State, StatesGroup
#from keyboard.prof_keyboards import make_row_keyboard

weather_names=['/Погода', 'Инфо']


router = Router()
#class ChoiseProfName(StatesGroup):
#   choise_prof_name = State()
#    choise_prof_graders = State()

@router.message(F.text.lower() == 'погода')
async def mes_weather(message: types.Message):
  #  name = message.chat.first_name
    temp = weath.weathers()
    await message.answer(f'Погода нынче такая  {temp}')
@router.message(Command('weather'))
async def cmd_weather(message: types.Message):
  #  name = message.chat.first_name
    await message.answer(f'Now weather is cold')
