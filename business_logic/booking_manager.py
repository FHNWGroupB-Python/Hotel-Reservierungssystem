import model
import data_access


class BookingManager:
    def __init__(self):
        self.__booking_da = data_access.BookingDataAccess()

    def create_booking(self, customer: model.Customer, hotel: model.Hotel, number_of_guests: int, check_in: str, check_out: str) -> model.Booking:
        return self.__booking_da.create_booking(customer, hotel, number_of_guests, check_in, check_out)

    def update_booking(self, booking: model.Booking) -> None:
        self.__booking_da.update_booking(booking)

    def cancel_booking(self, booking: model.Booking) -> None:
        self.__booking_da.cancel_booking(booking)

    def show_booking_details(self, booking: model.Booking) -> str:
        return booking.get_details()