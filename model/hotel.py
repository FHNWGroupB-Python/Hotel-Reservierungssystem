from model.room import Room
from model.facility import Facilities
from model.address import Address
from model.booking import Booking

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
        self.address = Address # Aggregation (Adresse existiert unabhängig vom Hotel)
        self.rooms = [
            Room(
                roomid = i,
                room_number = i,
                room_type = "",
                price_per_night = 0.0,
                hotel = self
            )
            for i in range(1, number_of_rooms + 1)
        ] # Komposition (Das Zimmer gehört fest zu einem Hotel)
        self.bookings = [] # Komposition (Buchung gehört fest zu einem Hotel)
        self.facilities = [] # Assoziation: (Dienste können unabhängig existieren)

    def add_room(self, room: "Room"):
        room.hotel = self
        self.rooms.append(room)

    def add_facility(self, facility: "Facilities"):
        self.facilities.append(facility)

    def add_booking(self, booking: "Booking"):
        booking.hotel = self
        self.bookings.append(booking)
