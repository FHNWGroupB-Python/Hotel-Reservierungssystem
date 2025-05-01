# Assoziation, Aggregation, Komposition

class Hotel:
    def __init__(self, hotelid, hotel_name, street, city, zip_code, country, stars, number_of_rooms):
        self.hotelid = hotelid
        self.hotel_name = hotel_name
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.country = country
        self.stars = stars
        self.number_of_rooms = number_of_rooms
    # Aggregation: Zimmer sind Teil des Hotels, können aber unabhängig existieren
        self.rooms = []
    # Assoziation: Dienste können unabhängig existieren
        self.services = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_service(self, service):
        self.services.append(service)

class Room:
    def __init__(self, roomid, hotelid, room_number, room_type, price_per_night):
        self.roomid = roomid
        self.hotelid = hotelid
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in vars(self).items())

class AdditionalService:
    def __init__(self, additionalserviceid, additional_service, additional_service_price):
        self.additionalserviceid = additionalserviceid
        self.additional_service = additional_service
        self.additional_service_price = additional_service_price

    def __str__(self):
        return ', '.join(f'{key}: {value}' for key, value in vars(self).items())
