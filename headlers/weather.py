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

@router.message(Command('Погода'))
async def cmd_weather(message: types.Message):
  #  name = message.chat.first_name
    await message.answer(f'Погода нынче такая ')


# Хэндлер на команду /
#@router.message(Command('prof'))
#async def cmd_prof(message: types.Message, state: FSMContext):
#    name = message.chat.first_name
#    await message.answer(f'Привет, {name}, выбери профессию', reply_markup=make_row_keyboard(avalabel_prof_names))
#    await state.set_state(ChoiseProfName.choise_prof_name)