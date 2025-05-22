from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class RoomTypeDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_room_type(self, room_type: model.RoomType) -> model.RoomType:
        sql = """
        INSERT INTO RoomType (description, max_guests) VALUES (?, ?)
        """
        params = (
            room_type.description,
            room_type.max_guests
        )
        self.execute(sql, params)

    def update_room_type(self, room_type: model.RoomType) -> model.RoomType:
        sql = """
        UPDATE RoomType SET description = ?, max_guest = ? WHERE room_type_id = ?
        """
        params = tuple([
            room_type.description,
            room_type.max_guests
        ])
        self.execute(sql, params)

    def delete_room_type(self, room_type: model.RoomType) -> model.RoomType:
        sql = """
        DELETE FROM RoomType WHERE room_type_id = ?
        """
        params = (
            room_type.room_type_id,
        )
        self.execute(sql, params)



