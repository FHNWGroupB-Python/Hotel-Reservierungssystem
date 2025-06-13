from __future__ import annotations
from datetime import date

import pandas as pd

import model
from data_access.base_dal import BaseDAL
from model.booking import Booking
from model.hotel import Hotel
from model.room import Room
from model.guest import Guest

class BookingDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_booking(
        self,
        guest: model.Guest,
        room: model.Room,
        check_in_date: date,
        check_out_date: date,
        total_amount: float
    ) -> model.Booking:
        if check_in_date is None or check_out_date is None or total_amount is None:
            raise ValueError("Missing required fields")


        sql = """
        INSERT INTO Booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        params = (
            guest.guestid,
            room.room_id,
            check_in_date,
            check_out_date,
            int(False),  # SQLite kennt kein BOOLEAN
            total_amount
        )

        lastrowid, _ = self.execute(sql, params)
        return model.Booking(lastrowid, check_in_date, check_out_date, False, total_amount)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        if booking_id is None:
            raise ValueError("Booking ID is required")

        sql = """
        SELECT booking_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking WHERE booking_id = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, check_in, check_out, is_cancelled, total_amount = result
            return Booking(booking_id, check_in, check_out, bool(is_cancelled), total_amount)
        return None

    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """
        results = self.fetchall(sql)
        return [
            Booking(booking_id, check_in, check_out, bool(is_cancelled), total_amount)
            for (booking_id, check_in, check_out, is_cancelled, total_amount) in results
        ]

    def get_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT b.booking_id, b.check_in_date, b.check_out_date,
        g.guest_id, g.first_name, g.last_name, 
        r.room_id, r.room_number, 
        h.hotel_id, h.name 
        FROM Booking b        
        JOIN Guest g ON b.guest_id = g.guest_id        
        JOIN Room r ON b.room_id = r.room_id        
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        """
        results = self.fetchall(sql)

        bookings: list[Booking] = []
        for (
            booking_id,
            check_in_date,
            check_out_date,
            guest_id,
            first_name,
            last_name,
            room_id,
            room_number,
            hotel_id,
            hotel_name
        ) in results:
            hotel = Hotel(hotel_id, hotel_name, None)
            room = Room(room_id, room_number, None)
            room.hotel = hotel
            guest = Guest(guest_id, first_name, last_name, None)
            booking = Booking(
                booking_id,
                check_in_date,
                check_out_date,
                room,
                guest
            )
            booking.room = room
            booking.guest = guest
            bookings.append(booking)
        return bookings

    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, check_in_date, check_out_date, is_cancelled, total_amount FROM Booking
        """
        results = self.fetchall(sql)
        return [
            Booking(booking_id, check_in, check_out, bool(is_cancelled), total_amount)
            for (booking_id, check_in, check_out, is_cancelled, total_amount) in results
        ]

    def delete_booking(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE booking_id = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0

    def booking_exists(self, booking_id: int) -> bool:
        # SQL-Abfrage, um die Existenz der Buchung zu prüfen
        sql = "SELECT * FROM Booking WHERE booking_id = ?"
        result = self.fetchone(sql, (booking_id,))
        return result is not None

    def cancel_booking(self, booking_id: int) -> None:
        # Überprüfen, ob die Buchung bereits storniert ist
        if not booking_id:
            raise ValueError("Give a valid Booking ID")
        booking = self.read_booking_by_id(booking_id)
        if booking.is_cancelled:
            raise ValueError("Booking already cancelled.")

        else:
            sql = """Update Booking SET is_cancelled = ? WHERE booking_id = ?"""
            params = (1, booking_id)
            self.execute(sql, params)
            print(f"Booking with Booking Id {booking_id} cancelled successfully.")

    def get_famous_room_type(self) -> pd.Dataframe:
        sql = """
        SELECT room_type.description AS room_type, count(Booking.booking_id) AS bookings
        FROM Room
        join Room_Type on Room.type_id = Room_Type.type_id
        join Booking on Room.room_id = Booking.room_id
        GROUP BY Room_Type.type_id, Room_Type.description
        ORDER BY bookings DESC;
        """
        params = tuple()
        return pd.read_sql(sql, self._connect(), params=params)




