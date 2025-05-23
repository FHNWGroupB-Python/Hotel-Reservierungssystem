import model
import data_access


class BookingManager:
    def __init__(self):
        self.__booking_dal = data_access.BookingDAL(db_path = "database/hotel_reservation_sample.db")

    def create_booking(self, guest: model.Guest, hotel: model.Hotel, number_of_guests: int, check_in: str, check_out: str) -> model.Booking:
        return self.__booking_dal.create_booking(guest, hotel, number_of_guests, check_in, check_out)

    def update_booking(self, booking: model.Booking) -> None:
        self.__booking_dal.update_booking(booking)

    def cancel_booking(self, booking: model.Booking) -> None:
        self.__booking_dal.cancel_booking(booking)

    def show_booking_details(self, booking: model.Booking) -> str:
        return booking.get_details()