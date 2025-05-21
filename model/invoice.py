from __future__ import annotations

class Invoice:
    def __init__(self, invoiceid:int, issue_date: str, total_amount: float, booking = None):
        self.__invoiceid = invoiceid
        self.__issue_date = issue_date
        self.__total_amount = total_amount
        self.booking = booking

    @property
    def invoiceid(self):
        return self.__invoiceid

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def total_amount(self):
        return self.__total_amount

