# Konstruktoren

class Payment:
    def __init__ (self, paymentid: int, additional_service: str):
        self.paymentid = paymentid
        self.additional_service = additional_service

    def __str__(self):
        return(f"Rechnungsnummer: {self.paymentid}, Additional Service: {self.additional_service}")

class Booking:
    def __init__ (self, bookingid: int, number_of_guest:int, check_in: str, check_out: str, status: str):
        self.bookingid = bookingid
        self.number_of_guest = number_of_guest
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

    def __str__(self):
        return(f"Buchungsnummer: {self.bookingid}, Anzahl Gäste: {self.number_of_guest}",
               f"Checkin: {self.check_in}, Checkout: {self.check_out}, Status: {self.status}")

class Facilities:
    def __init__(self, facilityid: int, facility: str):
        self.facilityid = facilityid
        self.facility = facility

    def __str__(self):
        return(f"Einrichtung: {self.facility}")
