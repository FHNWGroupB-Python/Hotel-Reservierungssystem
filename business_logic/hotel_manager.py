from datetime import date

import model
import data_access



class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, name: str, stars: int, address:model.Address) -> model.Hotel:
        all_hotels = self.__hotel_dal.get_all_hotel_info()
        for hotel in all_hotels:
            print(f"Hotel: {hotel.name}, Adresse: {hotel.address.street}, {hotel.address.city}, {hotel.address.zip_code}")
            if hotel.name.strip().lower() == name.strip().lower() \
                and hotel.address.street.strip().lower() == address.street.strip().lower() \
                and hotel.address.city.strip().lower() == address.city.strip().lower() \
                and hotel.address.zip_code == address.zip_code:
                raise ValueError(f"Das Hotel '{hotel.name}' ist bereits vorhanden.")
        return self.__hotel_dal.create_hotel(name, stars, address) # TODO Logik einsetzen ob das Hotel bereits existiert

    def update_hotel(self, hotel:model.Hotel) -> model.Hotel:
        return self.__hotel_dal.update_hotel(hotel.hotel_id, hotel.name, hotel.stars)

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

    def search_hotels_by_city_and_availability(self, city: str, check_in_date: date, check_out_date: date) -> list[model.Hotel]:
        return self.__hotel_dal.search_hotels_by_city_and_availability(city, check_in_date, check_out_date) # TODO Logik für Verfügbarkeit der Checkin und Checkout erstellen

    def search_hotels_by_city_availability_stars_capacity(self, city: str, check_in_date: date, check_out_date: date, stars: int, max_guests: int) -> list[model.Hotel]:
        return self.__hotel_dal.search_hotels_by_city_availability_stars_capacity(city, check_in_date, check_out_date, stars, max_guests) # TODO Logik Verfügbarkeit einfügen

    def get_all_hotel_info(self) ->list[model.Hotel]:
        return self.__hotel_dal.get_all_hotel_info()

