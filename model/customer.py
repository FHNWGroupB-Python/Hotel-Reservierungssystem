from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.booking import Booking

class Customer:
    def __init__(self, customerid:int, first_name:str, last_name:str, phone:str, email:str):
        self.__customerid = customerid
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone = phone
        self.__email = email
        self.bookings = [] # Assoziation (Kunde in Verbindung 1-zu-n zu Buchung)

    def add_booking(self, booking: "Booking"):
        self.bookings.append(booking)

    @property
    def customerid(self):
        return self.__customerid

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
