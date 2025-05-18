from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.booking import Booking

class Invoice:
    def __init__(self, invoiceid:int, amount:str, status:str, invoice_date:str, booking: "Booking" = None):
        self.__invoiceid = invoiceid
        self.__amount = amount
        self.__status = status
        self.__invoice_date = invoice_date
        self.booking = booking # Referenz auf Booking 1-zu-1 Komposition

    @property
    def invoiceid(self):
        return self.__invoiceid

    @property
    def amount(self):
        return self.__amount

    @property
    def status(self):
        return self.__status

    @property
    def invoice_date(self):
        return self.__invoice_date

