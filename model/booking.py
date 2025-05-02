class Booking:
    def __init__ (self, bookingid: int, number_of_guest:int, check_in: str, check_out: str, status: str):
        self.bookingid = bookingid
        self.number_of_guest = number_of_guest
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

    def __str__(self):
        return (f"Buchungs ID: {self.bookingid}, Anzahl Gäste: {self.number_of_guest}",
               f"Checkin: {self.check_in}, Checkout: {self.check_out}, Status: {self.status}")