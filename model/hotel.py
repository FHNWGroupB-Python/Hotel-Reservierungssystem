from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.room import Room
    from model.address import Address

class Hotel:
    def __init__(self, hotelid:int, hotel_name:str, stars:int):
        self.__hotelid = hotelid
        self.__hotel_name = hotel_name
        self.__stars = stars
        self.__rooms = []
        self.address = None

    def add_room(self, room: "Room"):
        if room in self.__rooms:
            raise ValueError("Room already exists")
        if room.hotel is not None and room.hotel != self:
            raise ValueError("Room already assigned to another hotel")
        room.hotel = self
        self.__rooms.append(room)

    @property
    def hotelid(self):
        return self.__hotelid

    @property
    def hotel_name(self):
        return self.__hotel_name

    @hotel_name.setter
    def hotel_name(self, name:str) -> None:
        if not name:
            raise ValueError("hotel_name is required")
        if not isinstance(name, str):
            raise ValueError("hotel_name must be a string")
        self.__hotel_name = name

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, stars: int) -> None:
        if stars is None:
            raise ValueError("stars is required")
        if not isinstance(stars, int):
            raise ValueError("stars must be an integer")
        if not 1 <= stars <= 5:
            raise ValueError("stars must be between 1 and 5")
        self.__stars = stars
