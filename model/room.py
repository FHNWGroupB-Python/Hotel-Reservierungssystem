from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.hotel import Hotel

class Room:
    def __init__(self, roomid:int, room_number:int, price_per_night:float):
        self.__roomid = roomid
        self.__room_number = room_number
        self.__price_per_night = price_per_night
        self.hotel = None

    @property
    def hotel(self) -> "Hotel":
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel: "Hotel"):
        if self.hotel is not None and self.hotel != hotel:
            raise ValueError("Room is already assigned in another Hotel")
        self.__hotel = hotel

    @property
    def roomid(self):
        return self.__roomid

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

