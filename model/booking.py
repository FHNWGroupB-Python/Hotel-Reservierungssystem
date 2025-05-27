from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.invoice import Invoice
    from model.guest import Guest
    from model.room import Room

class Booking:
    def __init__ (self, booking_id: int, check_in_date: date, check_out_date: date, is_cancelled: bool, total_amount: float):
        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = is_cancelled
        self.__total_amount = total_amount
        self.invoice = None
        self.guest = None
        self.room = None


    def add_invoice(self, invoice: "Invoice"):
        self.invoice = invoice

    def add_guest(self, guest: "Guest"):
        self.guest = guest

    def add_room(self, room: "Room"):
        self.room = room

    @property
    def bookingid(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    @property
    def total_amount(self):
        return self.__total_amount

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value: bool):
        self.__is_cancelled = value
