from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboard.keyboards import kb1, kb2
from utilits.random_fox import fox

router=Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)
# Хэндлер на инфо
@router.message(F.text.lower() == 'инфо')
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Инфо', reply_markup=kb1)

# Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


# Хэндлер на команду /fox
@router.message(Command('/fox'))
@router.message(Command('/лиса'))
@router.message(F.text.lower() == 'покажи лису')
@router.message(F.text.lower() == 'показать лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
# await bot.send_photo(message.from_user.id, photo=img_fox)


# Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'найти лису' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

