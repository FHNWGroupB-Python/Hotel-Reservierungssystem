from model.room import Room

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

    #def add_service(self, service):
    #    self.services.append(service)