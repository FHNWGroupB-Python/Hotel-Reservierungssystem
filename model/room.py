from __future__ import annotations
from typing import TYPE_CHECKING

import model

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.room_type import RoomType

class Room:
    def __init__(self, room_id:int, room_number:int, price_per_night:float):
        self.__room_id = room_id
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.__hotel = None
        self.__room_type = None


    @property
    def hotel(self) -> "Hotel":
        return self.__hotel

    @property
    def room_type(self) -> "RoomType":
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type: "RoomType"):
        from model.room_type import RoomType
        if room_type and not isinstance(room_type, RoomType):
            raise ValueError("Room Type must be an instance of RoomType")
        self.__room_type = room_type

    @property
    def room_id(self):
        return self.__room_id

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number):
        if not isinstance(room_number, int):
            raise ValueError("room_number must be an integer")
        if not room_number > 0:
            raise ValueError("room_number must be greater than 0")
        self.__room_number = room_number

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if not isinstance(price_per_night, float):
            raise ValueError("price_per_night must be a float")
        if not price_per_night > 0:
            raise ValueError("price_per_night must be greater than 0")
        self.__price_per_night = price_per_night

