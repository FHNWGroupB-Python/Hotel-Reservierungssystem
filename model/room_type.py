from __future__ import annotations



class RoomType:
    def __init__(self, type_id: int, description: str, max_guests: int):
        self.__type_id = type_id
        self.__description = description
        self.__max_guests = max_guests

    @property
    def type_id(self):
        return self.__type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not description.strip():
            raise ValueError("Description cannot be empty")
        self.__description = description

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, max_guests):
        if not isinstance(max_guests, int):
            raise ValueError("Max guests must be an integer")
        if max_guests < 1:
            raise ValueError("Max guests must be greater than 0")
        self.__max_guests = max_guests

