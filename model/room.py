from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.additional_service import AdditionalService
    from model.hotel import Hotel

class Room:
    def __init__(self, roomid:int, room_number:int, room_type:str, price_per_night:float, hotel:"Hotel"):
        self.__roomid = roomid
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price_per_night = price_per_night # privates Attribut
        self.hotel = hotel
        self.additional_services = []  # Assoziation (Service kann unabhängig existieren)

    def add_hotel(self, hotel: "Hotel"):
        self.hotel = hotel

    def add_additional_service(self, additional_service: "AdditionalService"):
        self.additional_services.append(additional_service)

    @property
    def roomid(self):
        return self.__roomid

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, room_number):
        self.__room_number = room_number

    @property
    def room_type(self):
        return self.__room_type

    @room_type.setter
    def room_type(self, room_type):
        self.__room_type = room_type

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        self.__price_per_night = price_per_night

