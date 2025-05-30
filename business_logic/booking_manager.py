from datetime import date

import model
import data_access

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

    def cancel_booking(self, booking: model.Booking) -> None:
        self.__booking_dal.cancel_booking(booking)

    def show_booking_details(self, booking: model.Booking) -> str:
        return booking.get_details()