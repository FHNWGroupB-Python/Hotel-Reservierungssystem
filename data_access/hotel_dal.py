from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class HotelDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_hotel(self, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int) -> model.Hotel:
        sql = """
        INSERT INTO Hotel (hotel_name, street, city, zip_code, country, stars, number_of_rooms) VALUES (?,?,?,?,?,?,?)
        """
        params = (
            hotel_name,
            street,
            city,
            zip_code,
            country,
            stars,
            number_of_rooms
        )
        last_row_id = self.execute_sql(sql, params)
        return model.Hotel(last_row_id, hotel_name, street, city, zip_code, country, stars, number_of_rooms)

    def update_hotel(self, hotel: model.Hotel) -> None:
        if hotel is None:
            raise ValueError("Hotel cannot be None")

        sql = """
        UPDATE Hotel SET hotel_name = ?, street = ?, city = ?, zip_code = ?, country = ?, stars = ?, number_of_rooms = ? WHERE hotelid = ?
        """
        params = tuple([
            hotel.hotel_name,
            hotel.street,
            hotel.city,
            hotel.zip_code,
            hotel.country,
            hotel.stars,
            hotel.number_of_rooms,
            hotel.hotelid
        ])

        last_row_id, row_count = self.execute_sql(sql, params)


