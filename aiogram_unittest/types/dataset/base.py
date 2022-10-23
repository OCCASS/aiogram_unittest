from collections.abc import Mapping
from typing import Any
from typing import Union


class DatasetItem(Mapping):
    def __init__(self, data: dict, *, model=None, name=None):
        self._data = data
        self._name = name
        self._model = model

    @property
    def data(self) -> dict:
        return self._data

    @property
    def model(self) -> Any:
        return self._model

    def as_object(self, **replace_args) -> Union[Any, None]:
        """
        Return an object from dict

        :return: Any | None
        """
        try:
            if self._model and isinstance(self._data, dict):
                data = self._data.copy()
                data.update(**replace_args)
                return self._recursive_as_object(data, self._model)
            else:
                return None
        except (AttributeError, TypeError):
            return None

    def _recursive_as_object(self, data: dict, model: Any):
        """
        This method is converting dict data to object, if one of the params is the DatasetItem method will be
        recursive convert it

        :param data: the dict that should be as object
        :param model: the object that will be returned
        :return:
        """
        result_data = data.copy()
        for key, value in data.items():
            if isinstance(value, DatasetItem):
                result_data[key] = self._recursive_as_object(value.data, value.model)

        return model(**result_data)

    def __set_name__(self, owner, name):
        if not name.isupper():
            raise NameError("Name for helper item must be in uppercase!")

        if self._name is None:
            self._name = name

    def __iter__(self):
        return iter(self._data.keys())

    def __getitem__(self, item):
        return self._data[item]

    def __len__(self):
        return len(self._data)
