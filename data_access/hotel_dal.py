from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class HotelDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_hotel(self, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int) -> model.Hotel:
        if not hotel_name or not isinstance(hotel_name, str):
            raise ValueError("Hotel name can't be None or empty.")
        if not street or not isinstance(street, str):
            raise ValueError("Street can't be None or empty.")
        if not city or not isinstance(city, str):
            raise ValueError("City can't be None or empty.")
        if not zip_code or zip_code <= 0:
            raise ValueError("Zip code need's to be a positive integer.")
        if not country or not isinstance(country, str):
            raise ValueError("Country can't be None or empty.")
        if not isinstance(stars, int) or stars < 1 or stars > 5:
            raise ValueError("Stars need's to be an integer between 1 and 5.")
        if not isinstance(number_of_rooms, int) or number_of_rooms <= 0:
            raise ValueError("Number of rooms must be a positive integer.")

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

    def delete_hotel(self, hotel_id: int) -> None:
        if not hotel_id:
            raise ValueError("Hotel ID cannot be None or zero.")

        sql = """
        DELETE FROM Hotel WHERE hotelid = ?
        """
        params = tuple([hotel_id])
        last_row_id, row_count = self.execute(sql, params)