from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    avtor = State()
    books = State()


@questions_router.message(Command('stop'))
@questions_router.message(F.text == 'stop')
async def stop_question(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Опрос прерван')


@questions_router.message(Command('quest'))
async def start_quest(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer('Введите "stop" для выхода')
    await message.answer('Ваше имя: ')


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.age)
    await message.answer('Ваш возраст: ')


@questions_router.message(F.text, Questionaire.age)
async def process_age(message: types.Message, state: FSMContext):
    # check age
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(age) < 12 or int(age) > 100:
        await message.answer("Возраст должен быть от 12 до 100")
    else:
        await state.update_data(age=int(age))
        await state.set_state(Questionaire.gender)
        await message.answer('Ваш пол')
        await message.answer('Например: М, Ж')


@questions_router.message(F.text, Questionaire.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.avtor)
    await message.answer('Ваш любимый автор: ')


@questions_router.message(F.text, Questionaire.avtor)
async def process_books(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.books)
    await message.answer('Сколько вы прочитали книг?:')


@questions_router.message(F.text, Questionaire.books)
async def process_books(message: types.Message, state: FSMContext):
    await state.update_data(books=message.text)

    data = await state.get_data()
    print(data)
    await state.clear()
    await message.answer('Спасибо большое, вы прошли опрос')
