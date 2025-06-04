from __future__ import annotations
from datetime import date

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

    def update_hotel(self, hotel_id: int, name: str, stars: int) -> model.Hotel:
        sql = """
        UPDATE Hotel SET name = ?, stars = ? WHERE hotel_id = ?
        """
        params = tuple([
            name,
            stars,
            hotel_id
        ])
        self.execute(sql, params)
        return model.Hotel(name, stars, hotel_id)

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
        LEFT JOIN Address a ON h.address_id = a.address_id WHERE a.city LIKE (?) AND h.stars >= (?)
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
        WHERE a.city LIKE (?) AND rt.max_guests >= (?)
        """
        params = (
            city,
            max_guests
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

    def search_hotels_by_city_and_availability(self, city: str, check_in_date: date, check_out_date: date) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, 
        a.address_id, a.street, a.city, a.zip_code, 
        r.room_number, r.price_per_night, 
        rt.description, rt.max_guests, 
        b.check_in_date, b.check_out_date, b.is_cancelled
        FROM Hotel h
        LEFT JOIN Address a ON h.address_id = a.address_id
        LEFT JOIN Room r ON r.hotel_id = h.hotel_id
        LEFT JOIN Room_Type rt ON rt.type_id = r.room_id
        LEFT JOIN Booking b ON b.room_id = r.room_id
        AND b.is_cancelled = 0
        AND b.check_in_date < (?)
        AND b.check_out_date > (?)
        WHERE a.city LIKE (?) AND b.booking_id IS NULL
        """
        params = (
            check_in_date,
            check_out_date,
            city
        )
        rows = self.fetchall(sql, params)

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city, zip_code, room_number, price_per_night, description, max_guests, check_in_date, check_out_date, is_cancelled in rows:
            addr = Address(address_id, street, city, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotel.room_number = room_number
            hotel.price_per_night = price_per_night
            hotel.description = description
            hotel.max_guests = max_guests
            hotel.check_in_date = check_in_date
            hotel.check_out_date = check_out_date
            hotel.is_cancelled = is_cancelled
            hotels.append(hotel)
        return hotels

    def search_hotels_by_city_availability_stars_capacity(self, city: str, check_in_date: date, check_out_date: date, stars: int, max_guests: int) -> list[model.Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, 
        a.address_id, a.street, a.city, a.zip_code, 
        r.room_number, r.price_per_night, 
        rt.description, rt.max_guests, 
        b.check_in_date, b.check_out_date, b.is_cancelled
        FROM Hotel h
        LEFT JOIN Address a ON h.address_id = a.address_id
        LEFT JOIN Room r ON r.hotel_id = h.hotel_id
        LEFT JOIN Room_Type rt ON rt.type_id = r.room_id
        LEFT JOIN Booking b ON b.room_id = r.room_id
        AND b.is_cancelled = 0
        AND b.check_in_date < (?)
        AND b.check_out_date > (?)
        WHERE a.city LIKE (?) 
        AND h.stars >= (?) 
        AND rt.max_guests >= (?) 
        AND b.booking_id IS NULL
        """
        params = (
            check_in_date,
            check_out_date,
            city,
            stars,
            max_guests
        )
        rows = self.fetchall(sql, params)

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city, zip_code, room_number, price_per_night, description, max_guests, check_in_date, check_out_date, is_cancelled in rows:
            addr = Address(address_id, street, city, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotel.room_number = room_number
            hotel.price_per_night = price_per_night
            hotel.description = description
            hotel.max_guests = max_guests
            hotel.check_in_date = check_in_date
            hotel.check_out_date = check_out_date
            hotel.is_cancelled = is_cancelled
            hotels.append(hotel)
        return hotels

    def get_all_hotel_info(self) -> list[model.Hotel]:
        sql = """
        SELECT DISTINCT h.hotel_id, h.name, h.stars,
        a.address_id, a.street, a.city, a.zip_code 
        FROM Hotel h 
        LEFT JOIN Address a ON h.address_id = a.address_id
        """
        results = self.fetchall(sql)

        hotels: list[model.Hotel] = []
        for hotel_id, name, stars, address_id, street, city, zip_code in results:
            addr = Address(address_id, street, city, zip_code)
            hotel = model.Hotel(hotel_id, name, stars)
            hotel.address = addr
            hotels.append(hotel)
        return hotels
