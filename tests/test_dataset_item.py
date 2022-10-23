import unittest

from aiogram import types

from aiogram_unittest.types.dataset import DatasetItem


class TestDatasetItem(unittest.TestCase):
    def test_as_object(self):
        dataset_item = DatasetItem({"firstArg": 1, "secondArg": 2})
        self.assertEqual(dataset_item.as_object(), {"firstArg": 1, "secondArg": 2})
        self.assertEqual(dataset_item.as_object(firstArg=3), {"firstArg": 3, "secondArg": 2})
        self.assertEqual(dataset_item.as_object(thirdArg=3), {"firstArg": 1, "secondArg": 2, "thirdArg": 3})

    def test_as_object_converting(self):
        dataset_item = DatasetItem(
            {
                "id": 12345678,
                "is_bot": False,
                "first_name": "FirstName",
                "last_name": "LastName",
                "username": "username",
            },
            model=types.User,
        )
        self.assertEqual(
            dataset_item.as_object(),
            types.User(id=12345678, is_bot=False, first_name="FirstName", last_name="LastName", username="username"),
        )
        self.assertEqual(
            dataset_item.as_object(first_name="EditedFirstName"),
            types.User(
                id=12345678, is_bot=False, first_name="EditedFirstName", last_name="LastName", username="username"
            ),
        )
        self.assertEqual(
            dataset_item.as_object(language_code="ru"),
            types.User(
                id=12345678,
                is_bot=False,
                first_name="EditedFirstName",
                last_name="LastName",
                username="username",
                language_code="ru",
            ),
        )

    def test_as_object_converting_with_nesting(self):
        dataset_item = DatasetItem(
            {
                "message_id": 11223,
                "from": {
                    "id": 12345678,
                    "is_bot": False,
                    "first_name": "FirstName",
                    "last_name": "LastName",
                    "username": "username",
                },
                "chat": {
                    "id": 12345678,
                    "first_name": "FirstName",
                    "last_name": "LastName",
                    "username": "username",
                    "type": "private",
                },
                "date": 1508709711,
                "text": "Hi, world!",
            },
            model=types.Message,
        )
        self.assertEqual(
            dataset_item.as_object().to_python(),
            types.Message(
                message_id=11223,
                from_user=types.User(
                    id=12345678, is_bot=False, first_name="FirstName", last_name="LastName", username="username"
                ),
                chat=types.Chat(
                    id=12345678,
                    first_name="FirstName",
                    last_name="LastName",
                    username="username",
                    type=types.ChatType.PRIVATE,
                ),
                date=1508709711,
                text="Hi, world!",
            ).to_python(),
        )
