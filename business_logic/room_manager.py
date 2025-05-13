import model
import data_access

class RoomManager:
    def __init__(self):
        self.__room_da = data_access.RoomDataAccess()

    def create_room(self, hotel: model.Hotel, room_number: int, room_type: str, price: float) -> model.Room:
        return self.__room_da.create_room(hotel, room_number, room_type, price)

    def update_room(self, room: model.Room) -> None:
        self.__room_da.update_room(room)

    def delete_room(self, room: model.Room) -> None:
        self.__room_da.delete_room(room)

    def check_availability(self, hotel: model.Hotel, check_in: str, check_out: str) -> list[model.Room]:
        return self.__room_da.search_room_availability(hotel, check_in, check_out)

