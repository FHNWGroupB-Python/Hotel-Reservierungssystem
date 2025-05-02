class Room:
    def __init__(self, roomid:int, room_number:int, room_type:str, price_per_night:float, hotel:"Hotel"):
        self.roomid = roomid
        self.room_number = room_number
        self.room_type = room_type
        self.__price_per_night = price_per_night # privates Attribut
        self.hotel = hotel

    def __str__(self):
        return (', '.join(f'{key}: {value}' for key, value in vars(self).items()))