from datetime import date

import model
import data_access
from datetime import date

import model
import data_access
from model.user import requires_permission, User

class RoomManager:
    def __init__(self, db_path=None):
        self.__room_dal = data_access.RoomDAL(db_path)

    def create_room(self, hotel: model.Hotel) -> model.Room:
        return self.__room_dal.create_room(hotel)

    @requires_permission("update_room")
    def update_room(self, room: model.Room, user: User) -> None:
        self.__room_dal.update_room(room.room_id, room.room_number, room.price_per_night)

    def delete_room(self, room: model.Room) -> None:
        self.__room_dal.delete_room(room)

    def get_room_info_by_hotel(self, name: str) -> list[model.Room]:
        return self.__room_dal.get_room_info_by_hotel(name) # TODO Logik implementieren für try/except

    def get_available_rooms_by_date(self, check_in_date: date, check_out_date: date) -> list[model.Room]:
        return self.__room_dal.get_available_rooms_by_date(check_in_date, check_out_date) # TODO Logik für Datum ergänzen damit zuerst geprüft wird welches Zimmer frei ist

    @requires_permission("get_all_rooms_with_equipment")
    def get_all_rooms_with_equipment(self, user: User):
        return self.__room_dal.get_all_rooms_with_equipment()