import model
import data_access

class RoomTypeManager:
    def __init__(self):
        self.__room_type_dal = data_access.RoomTypeDAL(db_path = "database/hotel_reservation_sample.db")

    def create_room_type(self, room_type: model.RoomType) -> model.RoomType:
        return self.__room_type_dal.create_room_type(room_type)

    def update_room_type(self, room_type: model.RoomType) -> model.RoomType:
        return self.__room_type_dal.update_room_type(room_type)

    def delete_room_type(self, room_type: model.RoomType) -> model.RoomType:
        return self.__room_type_dal.delete_room_type(room_type)
