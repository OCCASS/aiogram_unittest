import unittest

from aiogram import types

from aiogram_unittest import Request, RequestType
from aiogram_unittest.dataset import MESSAGE, CALLBACK_QUERY
from aiogram_unittest.handler import MessageHandler, CallbackQueryHandler
from test_bot import message_handler, command_handler, message_handler_with_state, callback_query_handler, \
    callback_query_handler_with_state, States, test_callback_data


class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_message_handler(self):
        request = Request(request_handler=MessageHandler(message_handler))

        message = types.Message(**MESSAGE)
        message.text = 'Hello!'
        call_args = await request.query(message)

        answer_message = call_args[RequestType.SEND_MESSAGE][0]['text']
        self.assertEqual(answer_message, 'Hello!')

    async def test_command_handler(self):
        request = Request(request_handler=MessageHandler(command_handler, commands=['start']))

        message = types.Message(**MESSAGE)
        message.text = '/start'
        call_args = await request.query(message)

        answer_message = call_args[RequestType.SEND_MESSAGE][0]['text']
        self.assertEqual(answer_message, 'Hello, new user!')

    async def test_message_handler_with_state(self):
        request = Request(request_handler=MessageHandler(message_handler_with_state, state=States.state))

        message = types.Message(**MESSAGE)
        message.text = 'Hello, bot!'
        call_args = await request.query(message)

        answer_message = call_args[RequestType.SEND_MESSAGE][0]['text']
        self.assertEqual(answer_message, 'Hello, from state!')

    async def test_callback_query_handler_with_state(self):
        request = Request(request_handler=CallbackQueryHandler(
            callback_query_handler_with_state, test_callback_data.filter())
        )

        callback_data = test_callback_data.new(id='1', name='John')
        callback_query = types.CallbackQuery(**CALLBACK_QUERY, data=callback_data)
        call_args = await request.query(callback_query)

        answer_text = call_args[RequestType.ANSWER_CALLBACK_QUERY][0]['text']
        self.assertEqual(answer_text, 'Hello, from state!')

    async def test_callback_query_handler(self):
        request = Request(request_handler=CallbackQueryHandler(callback_query_handler, test_callback_data.filter()))

        callback_data = test_callback_data.new(id='1', name='John')
        callback_query = types.CallbackQuery(**CALLBACK_QUERY, data=callback_data, message=types.Message(**MESSAGE))
        call_args = await request.query(callback_query)

        answer_text = call_args[RequestType.SEND_MESSAGE][0]['text']
        self.assertEqual(answer_text, 'Hello!')
