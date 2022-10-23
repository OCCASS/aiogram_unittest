from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters.state import StatesGroup
from aiogram.utils.callback_data import CallbackData

test_callback_data = CallbackData("send_user", "id", "name")

bot = Bot("123456789:AABBCCDDEEFFaabbccddeeff-1234567890")
dp = Dispatcher(bot, storage=MemoryStorage())


class States(StatesGroup):
    state = State()
    state_1 = State()


@dp.message_handler(state="*")
async def message_handler(message: types.Message, state: FSMContext):
    await message.answer(message.text)


@dp.message_handler(commands=["start"], state="*")
async def command_handler(message: types.Message, state: FSMContext):
    await message.answer("Hello, new user!")


@dp.message_handler(state=States.state)
async def message_handler_with_state(message: types.Message, state: FSMContext):
    await message.reply("Hello, from state!")


@dp.message_handler(state=States.state_1)
async def message_handler_with_state_data(message: types.Message, state: FSMContext):
    data = await state.get_data()
    await message.answer(f'Info from state data: {data["info"]}')


@dp.callback_query_handler(test_callback_data.filter(), state="*")
async def callback_query_handler(callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    name = callback_data.get("name")
    await callback_query.message.answer(f"Hello, {name}")


@dp.callback_query_handler(test_callback_data.filter(), state=States.state)
async def callback_query_handler_with_state(
    callback_query: types.CallbackQuery, callback_data: dict, state: FSMContext
):
    await callback_query.answer("Hello, from state!")
