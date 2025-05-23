import model
import data_access

class RoomManager:
    def __init__(self):
        self.__room_dal = data_access.RoomDAL(db_path = "database/hotel_reservation_sample.db")

    def create_room(self, hotel: model.Hotel) -> model.Room:
        return self.__room_dal.create_room(hotel)

    def update_room(self, room: model.Room) -> None:
        self.__room_dal.update_room(room)

    def delete_room(self, room: model.Room) -> None:
        self.__room_dal.delete_room(room)
