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
        try:
            hotel_id, _ = self.execute(sql, params)
            return model.Hotel(hotel_id, hotel_name, street, city, zip_code, country, stars, number_of_rooms)
        except Exception as e:
            print(f"Error creating hotel: {e}")
            raise

        self.execute(sql, params)
        return model.Hotel(hotel_id=hotel_id,
                           hotel_name=hotel_name,
                           street=street,
                           city=city,
                           zip_code=zip_code,
                           country=country,
                           stars=stars,
                           number_of_rooms=number_of_rooms
                           )

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
        self.execute(sql, params)

    def delete_hotel(self, hotel_id: int) -> None:
        if not hotel_id:
            raise ValueError("Hotel ID cannot be None or zero.")

        sql = """
        DELETE FROM Hotel WHERE hotelid = ?
        """
        params = tuple([hotel_id])
        last_row_id, row_count = self.execute(sql, params)

    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        if not city or not isinstance(city, str):
            raise ValueError("City must be a non-empty string.")

        sql = """
        SELECT * FROM Hotel WHERE city = ?
        """
        params = (city,)
        rows = self.fetchall(sql, (city,))

        # Falls keine Ergebnisse gefunden werden, leere Liste zurückgeben
        if not rows:
            return []

        # Ergebnisse in Hotel-Objekte umwandeln
        hotels = []
        for row in rows:
            hotels.append(model.Hotel(
                hotelid=row[0],
                hotel_name=row[1],
                street=row[2],
                city=row[3],
                zip_code=row[4],
                country=row[5],
                stars=row[6],
                number_of_rooms=row[7]
            ))
        return hotels

    def search_hotels_by_stars(self, stars: int) -> list[model.Hotel]:
        if not isinstance(stars, int) or stars < 1 or stars > 5:
            raise ValueError("Stars must be an integer between 1 and 5.")

        sql = """
        SELECT hotelid, hotel_name, street, city, zip_code, country, stars, number_of_rooms FROM Hotel WHERE stars = ?
        """
        params = (stars, )
        rows = self.fetchall(sql, (stars,))

        # Falls keine Ergebnisse gefunden werden, leere Liste zurückgeben
        if not rows:
            return []

        # Ergebnisse in Hotel-Objekte umwandeln
        hotels = []
        for row in rows:
            hotels.append(model.Hotel(
                hotelid=row[0],
                hotel_name=row[1],
                street=row[2],
                city=row[3],
                zip_code=row[4],
                country=row[5],
                stars=row[6],
                number_of_rooms=row[7]
            ))
        return hotels

