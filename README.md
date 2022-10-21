# aiogram_unittest

<hr>

***aiogram_unittest*** is a testing library for bots written on <a href="https://github.com/aiogram/aiogram">aiogram</a>

## Examples

<hr>
<details>
<summary>📚 Click here to see simple examples</summary>

### Simple handler test

#### Simple bot:

```python
from aiogram import Bot, Dispatcher, types, executor

# Please, keep your bot tokens on environments, this code only example
bot = Bot('123456789:AABBCCDDEEFFaabbccddeeff-1234567890')
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)


```

#### Test cases:

```python
import unittest

from aiogram import types
from bot import echo

from aiogram_unittest import Request, RequestType
from aiogram_unittest.dataset import MESSAGE
from aiogram_unittest.handler import MessageHandler


class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_echo(self):
        request = Request(request_handler=MessageHandler(echo))

        message = types.Message(**MESSAGE)
        message.text = 'Hello, Bot!'
        call_args = await request.query(message)

        answer_text = call_args[RequestType.SEND_MESSAGE][0]['text']
        self.assertEqual(answer_text, 'Hello, Bot!')

```

<a href='https://OCCCAS/aiogram_unittest/examples'>More</a> examples
</details>

