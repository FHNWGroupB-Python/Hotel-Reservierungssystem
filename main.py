#Klassen
class Hotel:
    def __init__(self, hotelid:int, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int):
        self.hotelid = hotelid
        self.hotel_name = hotel_name
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country
        self.stars = stars
        self.number_of_rooms = number_of_rooms
    # Komposition (Das Zimmer gehört fest zu einem Hotel)
        self.rooms = [
            Room(
                roomid = i,
                room_number = i,
                room_type = "",
                price_per_night = 0.0,
                hotel = self
            )
            for i in range(1, number_of_rooms + 1)
        ]
    # Assoziation: (Dienste können unabhängig existieren)
        self.services = []

    def add_room(self, room: "Room"):
        room.hotel = self
        self.rooms.append(room)

    def add_service(self, service):
        self.services.append(service)

class Room:
    def __init__(self, roomid:int, room_number:int, room_type:str, price_per_night:float, hotel:"Hotel"):
        self.roomid = roomid
        self.room_number = room_number
        self.room_type = room_type
        self.__price_per_night = price_per_night # privates Attribut
        self.hotel = hotel

    def __str__(self):
        return (', '.join(f'{key}: {value}' for key, value in vars(self).items()))

class AdditionalService:
    def __init__(self, additionalserviceid, additional_service, additional_service_price):
        self.additionalserviceid = additionalserviceid
        self.additional_service = additional_service
        self.additional_service_price = additional_service_price

    def __str__(self):
        return (', '.join(f'{key}: {value}' for key, value in vars(self).items()))

class Payment:
    def __init__ (self, paymentid: int, additional_service: str):
        self.paymentid = paymentid
        self.additional_service = additional_service

    def __str__(self):
        return (f"Rechnungs ID: {self.paymentid}, Additional Service: {self.additional_service}")

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

class Facilities:
    def __init__(self, facilityid: int, facility: str):
        self.facilityid = facilityid
        self.facility = facility

    def __str__(self):
        return (f"Einrichtung: {self.facility}")

class address:
    def __init__(self, adressid:int, street:str, zip_code:int, city:str, country:str):
        self.adressid = adressid
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self):
        return (f"Adresse ID: {self.adressid}, street: {self.street}, zip_code: {self.zip_code}, city: {self.city}, country: {self.country}")

class customer:
    def __init__(self, customerid:int, first_name:str, last_name:str, phone:str, email:str):
        self.customerid = customerid
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"Kunden ID: {self.customerid}, first_name: {self.first_name}, last_name: {self.last_name}, phone: {self.phone}, email: {self.email}")

class invoice:
    def __init__(self, invoiceid:int, amount:str, status:str, invoice_date:str):
        self.invoiceid = invoiceid
        self.amount = amount
        self.status = status
        self.invoice_date = invoice_date

    def __str__(self):
        return (f"Invoice ID: {self.invoiceid}, Betrag: {self.amount}, status: {self.status}")
