from model.booking import Booking

class Payment:
    def __init__ (self, paymentid: int, additional_service: str):
        self.paymentid = paymentid
        self.additional_service = additional_service

    def __str__(self):
        return (f"Rechnungs ID: {self.paymentid}, Additional Service: {self.additional_service}")