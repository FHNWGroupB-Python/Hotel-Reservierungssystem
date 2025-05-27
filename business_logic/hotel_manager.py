import model
import data_access

from model.address import Address


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, name: str, stars: int, address) -> model.Hotel:
        self.__hotel_dal.create_hotel(name, stars, address)

    def update_hotel(self, hotel_id: model.Hotel) -> None:
        self.__hotel_dal.update_hotel(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_dal.delete_hotel(hotel_id)

    def search_hotels_by_stars(self, stars: int) -> None:
        self.__hotel_dal.search_hotels_by_stars(stars)

    def search_hotels_by_name(self, name: str) -> None:
        self.__hotel_dal.search_hotels_by_name(name)

    def search_hotels_by_address(self, address: str) -> None:
        self.__hotel_dal.search_hotels_by_address(address)