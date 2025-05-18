from __future__ import annotations

class PaymentMethod:
    def __init__ (self, paymentid: int, paymentmethod: str):
        self.__paymentid = paymentid
        self.__paymentmethod = paymentmethod

    @property
    def paymentid(self):
        return self.__paymentid

    @property
    def paymentmethod(self):
        return self.__paymentmethod
