from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class HotelDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Hotel(
        hotelid INTEGER PRIMARY KEY AUTOINCREMENT,
        hotel_name TEXT NOT NULL,
        street TEXT NOT NULL,
        city TEXT NOT NULL,
        zip_code INTEGER NOT NULL,
        country TEXT NOT NULL,
        stars INTEGER NOT NULL,
        number_of_rooms INTEGER NOT NULL)
        """
        self.execute(sql)

    def create_hotel(self, hotel_name:str, stars:int) -> model.Hotel:
        sql = """
        INSERT INTO Hotel (hotel_name, stars) VALUES (?,?)
        """
        params = (
            hotel_name,
            stars,
        )
        self.execute(sql, params)

    def update_hotel(self, hotel: model.Hotel) -> None:
        sql = """
        UPDATE Hotel SET hotel_name = ?, stars = ? WHERE hotelid = ?
        """
        params = tuple([
            hotel.hotel_name,
            hotel.stars,
        ])
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = """
        DELETE FROM Hotel WHERE hotelid = ?
        """
        params = tuple([hotel_id])
        self.execute(sql, params)

    def search_hotels_by_stars(self, stars: int) -> list[model.Hotel]:
        sql = """
        SELECT stars FROM Hotel WHERE stars = ?
        """
        params = (stars, )
        self.fetchall(sql, (stars,))

    def search_hotels_by_name(self, name: str) -> list[model.Hotel]:
        sql = """
        SELECT hotel_name FROM Hotel WHERE hotel_name LIKE ?
        """
        params = (name, )
        self.fetchall(sql, (name,))