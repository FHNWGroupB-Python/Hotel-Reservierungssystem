import model
import data_access

from model.address import Address


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, name: str, stars: int, address) -> model.Hotel:
        return self.__hotel_dal.create_hotel(name, stars, address) # TODO Logik einsetzen ob das Hotel bereits existiert

    def update_hotel(self, hotel_id: model.Hotel) -> None:
        self.__hotel_dal.update_hotel(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_dal.delete_hotel(hotel_id)

    def search_hotels_by_stars(self, stars: int) -> None:
        self.__hotel_dal.search_hotels_by_stars(stars)

    def search_hotels_by_name(self, name: str) -> None:
        self.__hotel_dal.search_hotels_by_name(name)

    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        return self.__hotel_dal.search_hotels_by_city(city)

    def search_hotels_by_city_and_stars(self, city: str, stars: int) -> list[model.Hotel]:
        return self.__hotel_dal.search_hotels_by_city_and_stars(city, stars)

    def search_hotels_by_city_and_room_capacity(self, city: str, max_guests: int) -> list[model.Hotel]:
        return self.__hotel_dal.search_hotels_by_city_and_room_capacity(city, max_guests)
