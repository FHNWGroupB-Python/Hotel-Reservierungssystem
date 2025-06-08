from datetime import date

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
        days = (check_out - check_in).days
        total_amount = days * room.price_per_night

        if room.room_type.max_guests < number_of_guests:
            raise Exception("Room does not have enough capacity")

        return self.__booking_dal.create_booking(guest, room, check_in, check_out, total_amount)

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

