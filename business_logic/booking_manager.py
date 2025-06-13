from datetime import date, timedelta

import pandas
import pandas as pd

import model
import data_access
from model.user import requires_permission, User


class BookingManager:
    def __init__(self):
        self.__booking_dal = data_access.BookingDAL()

    def create_booking(
            self,
            guest: model.Guest,
            room: model.Room,
            number_of_guests: int,
            check_in: date,
            check_out: date
    ) -> model.Booking:

        if room.room_type.max_guests < number_of_guests:
            raise Exception("Room does not have enough capacity")

        current_date = check_in
        total_amount = 0

        while current_date < check_out:
            daily_price = self.calculate_dynamic_price(room.price_per_night, current_date)
            total_amount += daily_price
            current_date += timedelta(days=1)

        return self.__booking_dal.create_booking(guest, room, check_in, check_out, total_amount)


    def calculate_dynamic_price(self, price_per_night: float, check_in_date: date) -> float:
        high_season = {6, 7, 8}  # Juni, Juli, August
        off_season = {1, 2, 11}  # Januar, Februar, November
        month = check_in_date.month

        if month in high_season:
            return price_per_night * 1.2  # 20% Aufschlag
        elif month in off_season:
            return price_per_night * 0.85  # 15% Rabatt
        else:
            return price_per_night


    def update_booking(self, booking: model.Booking) -> None:
        self.__booking_dal.update_booking(booking)

    def cancel_booking(self, booking_id: int) -> None:
        if not isinstance(booking_id, int) or booking_id <= 0:
            raise ValueError("Ungültige Buchungs-ID. Bitte geben Sie eine positive ganze Zahl ein.")
        if not self.__booking_dal.booking_exists(booking_id):
            raise ValueError(f"Die Buchung mit der ID {booking_id} existiert nicht.")
        self.__booking_dal.cancel_booking(booking_id)

    def show_booking_details(self, booking: model.Booking) -> str:
        return booking.get_details()

    @requires_permission("get_all_bookings")
    def get_all_bookings(self, user: User) -> list[model.Booking]:
        return self.__booking_dal.get_all_bookings()

    def get_famous_room_type(self) -> pd.DataFrame:
        return self.__booking_dal.get_famous_room_type()



