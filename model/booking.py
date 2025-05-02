from model.hotel import Hotel
from model.invoice import Invoice
from model.customer import Customer
from model.payment_method import Payment


class Booking:
    def __init__ (self, bookingid: int, number_of_guest:int, check_in: str, check_out: str, status: str, hotel: "Hotel"):
        self.bookingid = bookingid
        self.number_of_guest = number_of_guest
        self.check_in = check_in
        self.check_out = check_out
        self.status = status
        self.hotel = hotel # Referenz auf Hotel
        self.invoice = None # Komposition (Rechnung ist fixer Bestandteil einer Buchung)
        self.customer = None # Assoziation (Customer)
        self.payment = None # Assoziation (Rechnungsmethode)

    def __str__(self):
        return (f"Buchungs ID: {self.bookingid}, Anzahl Gäste: {self.number_of_guest}, Checkin: {self.check_in}, Checkout: {self.check_out}, Status: {self.status}")
