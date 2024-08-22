"""
В Python есть несколько способов реализовать динамические атрибуты.
В этой главе рассматриваются самые простые: декоратор @property и специальный метод __getattr__.

"""

from collections import abc


class FrozenJSON:

    def __init__(self, mapping):
        self.__data = dict(mapping)

    """
    Метод __getattr__ вызывается, только когда не существует атрибута с именем name.
    """
    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.name)

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

"""
Когда класс вызывается для создания экземпляра, Python вызывает специальный метод класса __new__
"""

class FrozenV2JSON:

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = dict(mapping)

    """
    Метод __getattr__ вызывается, только когда не существует атрибута с именем name.
    """
    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON.build(self.name)

import json


class Record:
    def __init__(self, **kwargs):
        """
        копирование в __dict__ отображения – быстрый способ создать сразу несколько
        атрибутов (bunch of attributes) экземпляра
        """
        self.__dict__.update(kwargs)

    def __repr__(self):
        return f'<{self.__class__.__name__} serial={self.serial!r}>'

    def load(self, data):
        records = {}
        for collection, raw_records in data.items():
            record_type = collection[:-1]
            for raw_record in raw_records:
                key = f'{record_type}.{raw_record["serial"]}'
                records[key] = Record(**raw_record)
        return records