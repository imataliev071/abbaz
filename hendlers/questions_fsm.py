from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from db.queries import save_questions

questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    car_marka = State()
    bm = State()
    how_cars = State()


@questions_router.message(Command('stop'))
@questions_router.message(F.text == 'stop')
async def stop_question(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('Опрос прерван')


@questions_router.message(Command('questions'))
async def start_quest(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer('Введите "stop" для выхода')
    await message.answer('Ваше имя: ')


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
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
        await state.update_data(car_marka=message.text)
        await state.set_state(Questionaire.car_marka)
        await message.answer('Ваша любимая марка?')


@questions_router.message(F.text, Questionaire.car_marka)
async def process_bm(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.bm)
    await state.update_data(bm=message.text)
    await message.answer('Объем мотора Mersedes s600? ')


@questions_router.message(F.text, Questionaire.bm)
async def process_how_cars(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.how_cars)
    await state.update_data(how_cars=message.text)
    await message.answer('Какая у вас машина?')


@questions_router.message(F.text, Questionaire.how_cars)
async def process_how_cars(message: types.Message, state: FSMContext):
    await state.update_data(how_cars=message.text)

    data_quest = await state.get_data()
    save_questions(data_quest)
    print(data_quest)
    await state.clear()
    await message.answer('Спасибо большое, вы прошли опрос')
