import inspect
from typing import Any, Dict, List
from unittest.mock import AsyncMock

from aiogram.utils.helper import Helper, Item

from .handler import RequestHandler


class RequestType(Helper):
    @classmethod
    def get_from_lowercase(cls, lower_case: str):
        for item in cls.all():
            if item == lower_case.upper():
                return item

        return None

    ADD_STICKER_TO_SET = Item()
    ANSWER_CALLBACK_QUERY = Item()
    ANSWER_INLINE_QUERY = Item()
    ANSWER_PRE_CHECKOUT_QUERY = Item()
    ANSWER_SHIPPING_QUERY = Item()
    ANSWER_WEB_APP_QUERY = Item()
    APPROVE_CHAT_JOIN_REQUEST = Item()
    BAN_CHAT_MEMBER = Item()
    BAN_CHAT_SENDER_CHAT = Item()
    CHECK_AUTH_WIDGET = Item()
    COPY_MESSAGE = Item()
    CREATE_CHAT_INVITE_LINK = Item()
    CREATE_INVOICE_LINK = Item()
    CREATE_NEW_STICKER_SET = Item()
    DECLINE_CHAT_JOIN_REQUEST = Item()
    DELETE_CHAT_PHOTO = Item()
    DELETE_CHAT_STICKER_SET = Item()
    DELETE_MESSAGE = Item()
    DELETE_MY_COMMANDS = Item()
    DELETE_STICKER_FROM_SET = Item()
    DELETE_WEBHOOK = Item()
    DOWNLOAD_FILE = Item()
    DOWNLOAD_FILE_BY_ID = Item()
    EDIT_CHAT_INVITE_LINK = Item()
    EDIT_MESSAGE_CAPTION = Item()
    EDIT_MESSAGE_LIVE_LOCATION = Item()
    EDIT_MESSAGE_MEDIA = Item()
    EDIT_MESSAGE_REPLY_MARKUP = Item()
    EDIT_MESSAGE_TEXT = Item()
    EXPORT_CHAT_INVITE_LINK = Item()
    FORWARD_MESSAGE = Item()
    GET = Item()
    GET_CHAT = Item()
    GET_CHAT_ADMINISTRATORS = Item()
    GET_CHAT_MEMBER = Item()
    GET_CHAT_MEMBER_COUNT = Item()
    GET_CHAT_MEMBERS_COUNT = Item()
    GET_CHAT_MENU_BUTTON = Item()
    GET_CURRENT = Item()
    GET_CUSTOM_EMOJI_STICKERS = Item()
    GET_FILE = Item()
    GET_FILE_URL = Item()
    GET_GAME_HIGH_SCORES = Item()
    GET_ME = Item()
    GET_MY_COMMANDS = Item()
    GET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = Item()
    GET_NEW_SESSION = Item()
    GET_SESSION = Item()
    GET_STICKER_SET = Item()
    GET_UPDATES = Item()
    GET_USER_PROFILE_PHOTOS = Item()
    GET_WEBHOOK_INFO = Item()
    KICK_CHAT_MEMBER = Item()
    LEAVE_CHAT = Item()
    PIN_CHAT_MESSAGE = Item()
    PROMOTE_CHAT_MEMBER = Item()
    REQUEST = Item()
    REQUEST_TIMEOUT = Item()
    RESTRICT_CHAT_MEMBER = Item()
    REVOKE_CHAT_INVITE_LINK = Item()
    SEND_ANIMATION = Item()
    SEND_AUDIO = Item()
    SEND_CHAT_ACTION = Item()
    SEND_CONTACT = Item()
    SEND_DICE = Item()
    SEND_DOCUMENT = Item()
    SEND_FILE = Item()
    SEND_GAME = Item()
    SEND_INVOICE = Item()
    SEND_LOCATION = Item()
    SEND_MEDIA_GROUP = Item()
    SEND_MESSAGE = Item()
    SEND_PHOTO = Item()
    SEND_POLL = Item()
    SEND_STICKER = Item()
    SEND_VENUE = Item()
    SEND_VIDEO = Item()
    SEND_VIDEO_NOTE = Item()
    SEND_VOICE = Item()
    SET_CHAT_ADMINISTRATOR_CUSTOM_TITLE = Item()
    SET_CHAT_DESCRIPTION = Item()
    SET_CHAT_MENU_BUTTON = Item()
    SET_CHAT_PERMISSIONS = Item()
    SET_CHAT_PHOTO = Item()
    SET_CHAT_STICKER_SET = Item()
    SET_CHAT_TITLE = Item()
    SET_CURRENT = Item()
    SET_GAME_SCORE = Item()
    SET_MY_COMMANDS = Item()
    SET_MY_DEFAULT_ADMINISTRATOR_RIGHTS = Item()
    SET_PASSPORT_DATA_ERRORS = Item()
    SET_STICKER_POSITION_IN_SET = Item()
    SET_STICKER_SET_THUMB = Item()
    SET_WEBHOOK = Item()
    STOP_MESSAGE_LIVE_LOCATION = Item()
    STOP_POLL = Item()
    UNBAN_CHAT_MEMBER = Item()
    UNBAN_CHAT_SENDER_CHAT = Item()
    UNPIN_ALL_CHAT_MESSAGES = Item()
    UNPIN_CHAT_MESSAGE = Item()
    UPLOAD_STICKER_FILE = Item()


class Request:
    def __init__(self, *, request_handler: RequestHandler):
        self._handler = request_handler

    async def query(self, *args, **kwargs) -> Dict[str, List[Dict[str, Any]]]:
        await self._handler(*args, **kwargs)
        return await self._get_called_functions_arguments()

    async def _get_called_functions_arguments(self) -> Dict[str, List[Dict[str, Any]]]:
        result = {}

        for name, method in self._handler.bot.__dict__.items():
            skip = (name.startswith('_'), name.endswith('_'), not inspect.iscoroutinefunction(method),
                    not isinstance(method, AsyncMock))
            if any(skip):
                continue

            if method.call_count > 0:
                trigger_type = RequestType.get_from_lowercase(name)
                if trigger_type is not None:
                    if trigger_type not in result:
                        result[trigger_type] = []

                    result[trigger_type].append(self._handler.parse_args(method.call_args))

        return result
