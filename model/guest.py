from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.booking import Booking

class Guest:
    def __init__(self, guestid:int, first_name:str, last_name:str, email:str):
        self.__guestid = guestid
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.bookings = []
        self.address = None

    def add_booking(self, booking: "Booking"):
        self.bookings.append(booking)

    @property
    def guestid(self):
        return self.__guestid

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise ValueError("First Name must be a string")
        if not first_name:
            raise ValueError("First Name is required")
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise ValueError("Last Name must be a string")
        if not last_name:
            raise ValueError("Last Name is required")
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not email:
            raise ValueError("Email is required")
        self.__email = email
