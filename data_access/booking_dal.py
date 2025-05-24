from __future__ import annotations

from data_access.base_dal import BaseDAL
from model.booking import Booking

class BookingDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_booking(
        self,
        booking_id: int,
        check_in_date: str,
        check_out_date: str,
        total_amount: float,
        is_cancelled: bool = False
    ) -> Booking:
        if check_in_date is None or check_out_date is None or total_amount is None:
            raise ValueError("Missing required fields")

        sql = """
        INSERT INTO Booking (BookingId, CheckInDate, CheckOutDate, IsCancelled, TotalAmount)
        VALUES (?, ?, ?, ?, ?)
        """
        params = (
            booking_id,
            check_in_date,
            check_out_date,
            int(is_cancelled),  # SQLite kennt kein BOOLEAN
            total_amount
        )

        self.execute(sql, params)
        return Booking(booking_id, check_in_date, check_out_date, is_cancelled, total_amount)

    def read_booking_by_id(self, booking_id: int) -> Booking | None:
        if booking_id is None:
            raise ValueError("Booking ID is required")

        sql = """
        SELECT BookingId, CheckInDate, CheckOutDate, IsCancelled, TotalAmount
        FROM Booking WHERE BookingId = ?
        """
        result = self.fetchone(sql, (booking_id,))
        if result:
            booking_id, check_in, check_out, is_cancelled, total_amount = result
            return Booking(booking_id, check_in, check_out, bool(is_cancelled), total_amount)
        return None

    def read_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT BookingId, CheckInDate, CheckOutDate, IsCancelled, TotalAmount FROM Booking
        """
        results = self.fetchall(sql)
        return [
            Booking(booking_id, check_in, check_out, bool(is_cancelled), total_amount)
            for (booking_id, check_in, check_out, is_cancelled, total_amount) in results
        ]

    def delete_booking(self, booking_id: int) -> bool:
        sql = "DELETE FROM Booking WHERE BookingId = ?"
        _, rowcount = self.execute(sql, (booking_id,))
        return rowcount > 0

