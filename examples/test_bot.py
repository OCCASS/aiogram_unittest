from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData

test_callback_data = CallbackData('send_user', 'id', 'name')

bot = Bot('123456789:AABBCCDDEEFFaabbccddeeff-1234567890')
dp = Dispatcher(bot, storage=MemoryStorage())


class States(StatesGroup):
    state = State()


@dp.message_handler(state='*')
async def message_handler(message: types.Message, state: FSMContext):
    await message.answer(message.text)


@dp.message_handler(commands=['start'], state='*')
async def command_handler(message: types.Message, state: FSMContext):
    await message.answer('Hello, new user!')


@dp.message_handler(state=States.state)
async def message_handler_with_state(message: types.Message, state: FSMContext):
    await message.reply('Hello, from state!')


@dp.callback_query_handler(test_callback_data.filter(), state='*')
async def callback_query_handler(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await callback_query.message.answer('Hello!')


@dp.callback_query_handler(test_callback_data.filter(), state=States.state)
async def callback_query_handler_with_state(
        callback_query: types.CallbackQuery,
        callback_data: dict, state: FSMContext):
    await callback_query.answer('Hello, from state!')
