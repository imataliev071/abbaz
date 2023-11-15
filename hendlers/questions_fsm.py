from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    country = State()


@questions_router.message(Command('stop'))
@questions_router.message(F.text == 'stop')
async def stop_question(message: types.Message, state: FSMContext):
    # await state.update_data(name=message.text)
    await state.set_state(Questionaire.name)



@questions_router.message(Command('quest'))
async def start_quest(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer('Ваше имя: ')


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.age)
    await message.answer('Ваш возраст: ')


@questions_router.message(F.text, Questionaire.age)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.age)
    await message.answer('Ваш пол: ')


@questions_router.message(F.text, Questionaire.gender)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.age)
    await message.answer('Ваша страна: ')


@questions_router.message(F.text, Questionaire.country)
async def process_name(message: types.Message, state: FSMContext):
    await message.answer('Спасибо')
