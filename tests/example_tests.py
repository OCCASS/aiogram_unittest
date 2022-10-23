import unittest

from test_bot import callback_query_handler
from test_bot import callback_query_handler_with_state
from test_bot import command_handler
from test_bot import message_handler
from test_bot import message_handler_with_state
from test_bot import States
from test_bot import test_callback_data

from aiogram_unittest import Requester
from aiogram_unittest.handler import CallbackQueryHandler
from aiogram_unittest.handler import MessageHandler
from aiogram_unittest.types.dataset import CALLBACK_QUERY
from aiogram_unittest.types.dataset import MESSAGE


class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_message_handler(self):
        requester = Requester(request_handler=MessageHandler(message_handler))

        message = MESSAGE.as_object(text="Hello!")
        calls = await requester.query(message)

        answer_message = calls.send_message[0].text
        self.assertEqual(answer_message, "Hello!")

    async def test_command_handler(self):
        requester = Requester(request_handler=MessageHandler(command_handler, commands=["start"]))

        message = MESSAGE.as_object(text="/start")
        calls = await requester.query(message)

        answer_message = calls.send_message[0].text
        self.assertEqual(answer_message, "Hello, new user!")

    async def test_message_handler_with_state(self):
        requester = Requester(request_handler=MessageHandler(message_handler_with_state, state=States.state))

        message = MESSAGE.as_object(text="Hello, bot!")
        calls = await requester.query(message)

        answer_message = calls.send_message[0].text
        self.assertEqual(answer_message, "Hello, from state!")

    async def test_callback_query_handler_with_state(self):
        requester = Requester(
            request_handler=CallbackQueryHandler(callback_query_handler_with_state, test_callback_data.filter())
        )

        callback_query = CALLBACK_QUERY.as_object(data=test_callback_data.new(id="1", name="John"))
        calls = await requester.query(callback_query)

        answer_text = calls.answer_callback_query[0].text
        self.assertEqual(answer_text, "Hello, from state!")

    async def test_callback_query_handler(self):
        requester = Requester(request_handler=CallbackQueryHandler(callback_query_handler, test_callback_data.filter()))

        callback_query = CALLBACK_QUERY.as_object(
            data=test_callback_data.new(id="1", name="John"), message=MESSAGE.as_object(text="Hello world!")
        )
        calls = await requester.query(callback_query)

        answer_text = calls.send_message[0].text
        self.assertEqual(answer_text, "Hello, John")

        callback_query = CALLBACK_QUERY.as_object(
            data=test_callback_data.new(id="1", name="Mike"), message=MESSAGE.as_object(text="Hello world!")
        )
        calls = await requester.query(callback_query)

        answer_text = calls.send_message[0].text
        self.assertEqual(answer_text, "Hello, Mike")
