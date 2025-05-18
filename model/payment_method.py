from __future__ import annotations

class PaymentMethod:
    def __init__ (self, paymentid: int, additional_service: str):
        self.__paymentid = paymentid
        self.__additional_service = additional_service

    @property
    def paymentid(self):
        return self.__paymentid

    @property
    def additional_service(self):
        return self.__additional_service
