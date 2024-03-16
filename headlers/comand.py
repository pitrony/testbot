from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboard.keyboards import kb1, kb2
from utilits.random_fox import fox

router = Router()

# Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)
# Хэндлер на инфо
@router.message(F.text.lower() == 'инфо')
async def cmd_info(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Это тестовый бот создал Фролов Алексей email: frolov25alesha@gmail.com', reply_markup=kb1)
@router.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(help_mess, reply_markup=types.ReplyKeyboardRemove())

# Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}',  reply_markup=types.ReplyKeyboardRemove())
# Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(F.text.lower() == 'лиса')
@router.message(F.text.lower() == 'покажи лису')
@router.message(F.text.lower() == 'показать лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
# await bot.send_photo(message.from_user.id, photo=img_fox)
help_mess = ('/start - Старт бота ' + '\n' + 'help -  команды бота\n пока - пока от бота\n' +
             '/fox, лиса, покажи лису, показать лису - показать картинку с лисой\n /stop - Стоп бота\n'+
             '/prof - пример по цепочкам выбора\n ты кто - вывод емоджи\n'+
             '/weather - погода в городах,\n'+
             'погода в спб - погода в Санкт-Петербурге,\nпогода в москве - погода в Москве')

# Хендлер на текстовые сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'help' == msg_user:
        await message.answer(help_mess)
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'найти лису' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')

