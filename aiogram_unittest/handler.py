from typing import Callable, Any

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .args_parser import ArgumentsParser
from .dataset import USER, CHAT
from .utils import initialize_bot


class RequestHandler:
    def __init__(self, argument_parser: Callable):
        self._argument_parser = argument_parser
        self.bot = initialize_bot()
        self.dp = Dispatcher(self.bot, storage=MemoryStorage())

        Bot.set_current(self.bot)
        Dispatcher.set_current(self.dp)
        types.User.set_current(types.User(**USER))
        types.Chat.set_current(types.Chat(**CHAT))

    def parse_args(self, call_args: Any) -> dict:
        if call_args is None:
            return {}

        return self._argument_parser(call_args)

    async def __call__(self, *args, **kwargs):
        raise NotImplementedError


class MessageHandler(RequestHandler):
    def __init__(
            self, callback, *custom_filters: Any, commands=None, regexp=None, content_types=None, state=None,
            run_rask=None, **kwargs):
        super().__init__(ArgumentsParser.get_send_message_args)
        self._callback = callback
        self._custom_filters = custom_filters
        self._commands = commands
        self._regexp = regexp
        self._content_types = content_types
        self._state = state
        self._run_task = run_rask

    async def __call__(self, message: types.Message):
        self.dp.register_message_handler(self._callback, *self._custom_filters, commands=self._commands,
                                         regexp=self._regexp, content_types=self._content_types, state=self._state,
                                         run_task=self._run_task)
        if self._state:
            await self.dp.current_state().set_state(self._state)
        await self.dp.process_update(types.Update(message=message))


class CallbackQueryHandler(RequestHandler):
    def __init__(self, callback, *custom_filters, state=None, run_task=None, **kwargs):
        super().__init__(ArgumentsParser.get_answer_callback_query_args)
        self._callback = callback
        self._custom_filters = custom_filters
        self._state = state
        self._run_task = run_task

    async def __call__(self, callback_query: types.CallbackQuery):
        self.dp.register_callback_query_handler(self._callback, *self._custom_filters, state=self._state,
                                                run_task=self._run_task)
        if self._state:
            await self.dp.current_state().set_state(self._state)
        await self.dp.process_update(types.Update(callback_query=callback_query))
