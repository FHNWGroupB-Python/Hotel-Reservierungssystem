from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.room import Room
    from model.address import Address

class Hotel:
    def __init__(self, hotel_id:int, name:str, stars:int):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__rooms = []                  # Liste der Räume von Hotel
        self.address = None

    def add_room(self, room: "Room"):
        if room in self.__rooms:
            raise ValueError("Room already exists")
        if room.hotel is not None and room.hotel != self:
            raise ValueError("Room already assigned to another hotel")
        self.__rooms.append(room)
        room._Room__hotel = self

    @property
    def rooms(self) -> list["Room"]:
        return self.__rooms

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name:str) -> None:
        if not name:
            raise ValueError("hotel_name is required")
        if not isinstance(name, str):
            raise ValueError("hotel_name must be a string")
        self.__name = name

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
