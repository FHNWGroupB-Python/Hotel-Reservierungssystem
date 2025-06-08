from __future__ import annotations

from datetime import date

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

    def get_available_rooms_by_date(self, check_in_date: date, check_out_date: date) -> list[model.Room]:
        sql = """
        SELECT r.room_id, room_number, r.price_per_night, 
        rt.type_id, rt.description, rt.max_guests, 
        h.name, h.stars, 
        b.check_in_date, b.check_out_date, b.is_cancelled
        FROM Room r
        JOIN Hotel h on r.hotel_id = h.hotel_id
        JOIN Room_Type rt ON rt.type_id = r.room_id
        LEFT JOIN Booking b on b.booking_id = r.room_id
        AND b.is_cancelled = 0
        AND b.check_in_date < ?
        AND b.check_out_date > ?
        WHERE b.booking_id IS NULL
          """
        params = (
            check_in_date,
            check_out_date,
        )
        rows = self.fetchall(sql, params)

        rooms: list[model.Room] = []
        for room_id, room_number, price_per_night, type_id, description, max_guests, name, stars, check_in_date, check_out_date, is_cancelled in rows:
            room_type = model.RoomType(type_id, description, max_guests)
            room = model.Room(room_id, room_number, price_per_night)
            room.check_in_date = check_in_date
            room.check_out_date = check_out_date
            room.is_cancelled = is_cancelled
            room.room_type = room_type
            rooms.append(room)
        return rooms

    def get_all_rooms_with_equipment(self):
        # Room -> list of facilities

        from model.room import Room
        from model.hotel import Hotel
        from model.room_type import RoomType
        from model.facility import Facility

        def get_all_rooms_with_equipment(self):
            conn = self._get_connection()
            cursor = conn.cursor()

            query = """
                SELECT 
                    r.roomid, r.number, r.price_per_night,
                    rt.room_type_id, rt.name AS room_type,
                    h.hotelid, h.name AS hotel_name,
                    f.facilityid, f.name AS facility_name
                FROM Room r
                JOIN RoomType rt ON r.room_type_id = rt.room_type_id
                JOIN Hotel h ON r.hotelid = h.hotelid
                LEFT JOIN RoomFacility rf ON r.roomid = rf.roomid
                LEFT JOIN Facility f ON rf.facilityid = f.facilityid
                ORDER BY r.roomid
                """

            cursor.execute(query)
            rows = cursor.fetchall()
            print(rows)

            cursor.execute("SELECT COUNT(*) FROM Room")
            print("Anzahl Zimmer:", cursor.fetchone())

            rooms = {}
            for row in rows:
                roomid = row[0]

                if roomid not in rooms:
                    room_type = RoomType(row[3], row[4], None)
                    hotel = Hotel(row[5], row[6], None)
                    room = Room(roomid, row[1], row[2])
                    room.room_type = room_type
                    room.hotel = hotel
                    room.equipment = []
                    rooms[roomid] = room

                facility_id = row[7]
                facility_name = row[8]
                if facility_id and facility_name:
                    facility = Facility(facility_id, facility_name)
                    rooms[roomid].equipment.append(facility)

            return list(rooms.values())



