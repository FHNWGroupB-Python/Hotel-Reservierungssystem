from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class RoomDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Room(
        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hotel_id INTEGER NOT NULL,
        room_type TEXT NOT NULL,
        max_guests INTEGER NOT NULL,
        description TEXT,
        price_per_night REAL NOT NULL,
        amenities TEXT)
        """
        self.execute(sql)

    def create_room(self, room_id: int, room_number: int, price_per_night: float):
        sql = """
        INSERT INTO Room (room_id, hotel_id, room_number, price_per_night) VALUES (?,?,?,?)
        """
        params = (
            room_id,
            room_number,
            price_per_night,
        )
        self.execute(sql, params)

    def update_room(self, room_id: int, room_number: int, price_per_night: float):
        sql = """
        UPDATE Room SET room_number = ?, price_per_night = ? WHERE room_id = ?
        """
        params = tuple([
            room_number,
            price_per_night,
        ])
        self.execute(sql, params)

    def delete_room(self, room_id: int):
        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        params = tuple([room_id])
        self.execute(sql, params)

    def get_room_info_by_hotel(self, name: str) -> list[model.Room]:
        sql = """
        SELECT r.room_id, room_number, r.price_per_night, rt.type_id,rt.description, rt.max_guests, h.hotel_id, h.name, h.stars
        FROM Room r
        JOIN Hotel h on r.hotel_id = h.hotel_id
        JOIN Room_Type rt ON rt.type_id = r.room_id
        WHERE h.name = (?)
        """
        params = (
            name,
        )
        rows = self.fetchall(sql, params)

        rooms: list[model.Room] = []
        for room_id, room_number, price_per_night, type_id, description, max_guests, hotel_id, name, stars in rows:

            room_type = model.RoomType(type_id, description, max_guests)
            room = model.Room(room_id, room_number, price_per_night)
            room.room_type = room_type
            rooms.append(room)
        return rooms

