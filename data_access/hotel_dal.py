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

    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code FROM Hotel h
        LEFT JOIN Address a ON h.address_id = a.address_id WHERE a.city LIKE ?
        """
        params = (
            city
        )
        rows = self.fetchall(sql, (city,))

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city_name, zip_code in rows:
            addr = Address(address_id, street, city_name, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotels.append(hotel)
        return hotels

    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code FROM Hotel h
        LEFT JOIN Address a ON h.address_id = a.address_id WHERE a.city LIKE ? AND h.stars >= ?
        """
        params = (
            city,
            stars
        )
        rows = self.fetchall(sql, (city, stars))

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city_name, zip_code in rows:
            addr = Address(address_id, street, city_name, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotels.append(hotel)
        return hotels

    def search_hotels_by_city_and_room_capacity(self, city: str, max_guests: int) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, a.address_id, a.street, a.city, a.zip_code, r.room_number, r.price_per_night, rt.description, rt.max_guests FROM Hotel h 
        LEFT JOIN Address a ON h.address_id = a.address_id
        JOIN Room r ON r.hotel_id = h.hotel_id
        JOIN Room_Type rt ON rt.type_id = r.room_id
        WHERE a.city LIKE ? AND rt.max_guests >= ?
        """
        params = (
            city,
            max_guests,
        )
        rows = self.fetchall(sql, params)

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city_name, zip_code, room_number, price_per_night, description, max_guests in rows:
            addr = Address(address_id, street, city_name, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotel.room_number = room_number
            hotel.price_per_night = price_per_night
            hotel.description = description
            hotel.max_guests = max_guests
            hotels.append(hotel)
        return hotels