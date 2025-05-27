from __future__ import annotations

import model
from model.address import Address

from data_access.base_dal import BaseDAL

class HotelDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_hotel(self,
                     name:str,
                     stars:int,
                     address: model.Address
                     ) -> model.Hotel:
        sql = """
        INSERT INTO Hotel (name, stars, address_id) 
        VALUES (?, ?, ?)
        """
        params = (
            name,
            stars,
            address.address_id
        )
        lastrowid, _ = self.execute(sql, params)
        return model.Hotel(lastrowid, name, stars)

    def update_hotel(self, hotel: model.Hotel) -> None:
        sql = """
        UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?
        """
        params = tuple([
            hotel.name,
            hotel.stars,
        ])
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        sql = """
        DELETE FROM Hotel WHERE hotel_id = ?
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
        SELECT name FROM Hotel WHERE name LIKE ?
        """
        params = (name, )
        self.fetchall(sql, (name,))

    def search_hotels_by_address(self, address: str) -> None:
        sql = """
        SELECT * FROM Hotel LEFT JOIN Address ON Hotel.address_id = Address.address_id WHERE city LIKE ?
        """
        params = (
            address
        )
        self.fetchall(sql, (address,))