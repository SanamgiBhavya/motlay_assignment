from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def get_list_of_values(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def get_list_of_tuples(cls):
        return tuple(map(lambda c: (c.name, c.value), cls))
