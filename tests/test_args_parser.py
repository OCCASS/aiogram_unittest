import unittest

from aiogram_unittest.args_parser import ArgumentsParser
from aiogram_unittest.utils import initialize_bot


class TestArgsParser(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self._bot = initialize_bot()

    async def test_converting(self):
        await self._bot.send_message(chat_id=12345678, text="Hello, Bot!", parse_mode="Markdown")
        args = ArgumentsParser.get_send_message_args(self._bot.send_message.call_args)
        self.assertEqual(
            args.as_dict(),
            {
                "chat_id": 12345678,
                "text": "Hello, Bot!",
                "parse_mode": "Markdown",
                "entities": None,
                "disable_web_page_preview": None,
                "disable_notification": None,
                "protect_content": None,
                "reply_to_message_id": None,
                "allow_sending_without_reply": None,
                "reply_markup": None,
                "payload": None,
                "result": None,
            },
        )

    async def test_converting_with_none(self):
        args = ArgumentsParser.get_send_message_args(None)
        self.assertEqual(
            args.as_dict(),
            {
                "chat_id": None,
                "text": None,
                "parse_mode": None,
                "entities": None,
                "disable_web_page_preview": None,
                "disable_notification": None,
                "protect_content": None,
                "reply_to_message_id": None,
                "allow_sending_without_reply": None,
                "reply_markup": None,
                "payload": None,
                "result": None,
            },
        )

    async def test_converting_with_incorrect_args(self):
        await self._bot.send_message(arg1="arg1", arg2="arg2")
        args = ArgumentsParser.get_send_message_args(self._bot.send_message.call_args)
        self.assertEqual(
            args.as_dict(),
            {
                "chat_id": None,
                "text": None,
                "parse_mode": None,
                "entities": None,
                "disable_web_page_preview": None,
                "disable_notification": None,
                "protect_content": None,
                "reply_to_message_id": None,
                "allow_sending_without_reply": None,
                "reply_markup": None,
                "payload": None,
                "result": None,
            },
        )
