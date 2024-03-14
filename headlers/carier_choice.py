from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard.prof_keyboards import make_row_keyboard

avalabel_prof_names=['Разработчик', 'Аналитик', 'Тестировщик']
avalabel_prof_graders=['Джуниор', 'Мидл', 'Синьер']

router = Router()
class ChoiseProfName(StatesGroup):
    choise_prof_name = State()
    choise_prof_graders = State()

# Хэндлер на команду /prof
@router.message(Command('prof'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}, выбери профессию', reply_markup=make_row_keyboard(avalabel_prof_names))
    await state.set_state(ChoiseProfName.choise_prof_name)

# Хэндлер на выбор профессии
@router.message(ChoiseProfName.choise_prof_name, F.text.in_(avalabel_prof_names) )
async def prof_choise(message: types.Message, state: FSMContext):
    await state.update_data(prof_choise=message.text.lower())
    await message.answer(f'Спасибо за выбор профессии, выбери уровень ,', reply_markup=make_row_keyboard(avalabel_prof_graders))
    await state.set_state(ChoiseProfName.choise_prof_graders)

# Хэндлер на выбор профессии repeed
@router.message(ChoiseProfName.choise_prof_name )
async def prof_choise_incorect(message: types.Message):

    await message.answer(f'Я не знаю такой профессии', reply_markup=make_row_keyboard(avalabel_prof_names))

# Хэндлер на выбор уровня
@router.message(ChoiseProfName.choise_prof_graders, F.text.in_(avalabel_prof_graders) )
async def grade_choise(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f'Вы выбрали уровень {message.text.lower()}. Ваша профессия {user_data.get("prof_choise")} ,',
                         reply_markup=types.ReplyKeyboardRemove())
    await state.clear()

# Хэндлер на выбор профессии repeed
@router.message(ChoiseProfName.choise_prof_graders )
async def grade_choise_incorect(message: types.Message):

    await message.answer(f'Я не знаю такого уровня', reply_markup=make_row_keyboard(avalabel_prof_graders))



# Хэндлер на инфо
#@router.message(F.text.lower() == 'инфо')
#async def cmd_info(message: types.Message):
 #   name = message.chat.first_name
  #  await message.answer(f'Инфо', reply_markup=kb1)

# Хэндлер на команду /stop
#@router.message(Command('stop'))
#async def cmd_stop(message: types.Message):
  #  name = message.chat.first_name
   # await message.answer(f'Пока, {name}')