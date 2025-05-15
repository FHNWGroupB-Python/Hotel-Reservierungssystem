from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.additional_service import AdditionalService
    from model.hotel import Hotel

class Room:
    def __init__(self, roomid:int, room_number:int, room_type:str, price_per_night:float, hotel:"Hotel"):
        self.roomid = roomid
        self.room_number = room_number
        self.room_type = room_type
        self.__price_per_night = price_per_night # privates Attribut
        self.hotel = hotel
        self.additional_services = []  # Assoziation (Service kann unabhängig existieren)

    def __str__(self):
        return (', '.join(f'{key}: {value}' for key, value in vars(self).items()))

    def add_additional_service(self, additional_service: "AdditionalService"):
        self.additional_services.append(additional_service)