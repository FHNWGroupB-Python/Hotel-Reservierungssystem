from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class HotelDAL(Base_DAL):
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
            number_of_rooms,
            if hotel else None,
        )
        last_row_id = self.execute_sql(sql, params)
        return model.Hotel(last_row_id, hotel_name, street, city, zip_code, country, stars, number_of_rooms)

