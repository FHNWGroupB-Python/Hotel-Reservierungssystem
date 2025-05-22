from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.room import Room

class RoomType:
    def __init__(self, room_type_id: int, description: str, max_guests: int):
        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guests = max_guests
        self._rooms = []


    def add_room(self, room: "Room"):
        if room not in self._rooms:
            self._rooms.append(room)

    @property
    def rooms(self):
        return self._rooms

    @property
    def room_type_id(self):
        return self.__room_type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if isinstance(description, str):
            raise ValueError("Description must be a string")
        if not description:
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

