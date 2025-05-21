from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.hotel import Hotel
    from model.invoice import Invoice
    from model.guest import Customer

class Booking:
    def __init__ (self, bookingid: int, number_of_guest:int, check_in: str, check_out: str, status: str, hotel: "Hotel"):
        self.__bookingid = bookingid
        self.__number_of_guest = number_of_guest
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = status
        self.hotel = hotel
        self.invoice = None
        self.customer = None

    def add_invoice(self, invoice: "Invoice"):
        self.invoice = invoice

    def add_customer(self, customer: "Customer"):
        self.customer = customer

    @property
    def bookingid(self):
        return self.__bookingid

    @property
    def number_of_guest(self):
        return self.__number_of_guest

    @number_of_guest.setter
    def number_of_guest(self, number_of_guest):
        self.__number_of_guest = number_of_guest

    @property
    def check_in(self):
        return self.__check_in

    @check_in.setter
    def check_in(self, check_in):
        self.__check_in = check_in

    @property
    def check_out(self):
        return self.__check_out

    @check_out.setter
    def check_out(self, check_out):
        self.__check_out = check_out

    @property
    def status(self):
        return self.__status
