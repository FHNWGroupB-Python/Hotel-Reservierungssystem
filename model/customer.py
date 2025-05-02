class Customer:
    def __init__(self, customerid:int, first_name:str, last_name:str, phone:str, email:str):
        self.customerid = customerid
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.bookings = [] # Assoziation (Kunde in Verbindung 1-zu-n zu Buchung)

    def __str__(self):
        return (f"Kunden ID: {self.customerid}, first_name: {self.first_name}, last_name: {self.last_name}, phone: {self.phone}, email: {self.email}")
