from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.room import Room
    from model.facility import Facility
    from model.booking import Booking

class Hotel:
    def __init__(self, hotelid:int, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int):
        self.__hotelid = hotelid
        self.__hotel_name = hotel_name
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__country = country
        self.__stars = stars
        self.__number_of_rooms = number_of_rooms
        self.rooms = [
            Room(
                roomid = i,
                room_number = i,
                room_type = "",
                price_per_night = 0.0,
                hotel = self
            )
            for i in range(1, number_of_rooms + 1)
        ] # Komposition (Das Zimmer gehört fest zu einem Hotel)
        self.bookings = [] # Komposition (Buchung gehört fest zu einem Hotel)
        self.facilities = [] # Assoziation: (Dienste können unabhängig existieren)

    def add_room(self, room: "Room"):
        room.hotel = self
        self.rooms.append(room)

    def add_facility(self, facility: "Facilities"):
        self.facilities.append(facility)

    def add_booking(self, booking: "Booking"):
        booking.hotel = self
        self.bookings.append(booking)

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
    def street(self):
        return self.__street

    @street.setter
    def street(self, street:str) -> None:
        if not street:
            raise ValueError("street is required")
        if not isinstance(street, str):
            raise ValueError("street must be a string")
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city:str) -> None:
        if not city:
            raise ValueError("city is required")
        if not isinstance(city, str):
            raise ValueError("city must be a string")
        self.__city = city

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code:int) -> None:
        if not zip_code:
            raise ValueError("zip_code is required")
        if not isinstance(zip_code, int):
            raise ValueError("zip_code must be a int")
        self.__zip_code = zip_code

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country:str) -> None:
        if not country:
            raise ValueError("country is required")
        if not isinstance(country, str):
            raise ValueError("country must be a string")
        self.__country = country

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


