import model
import data_access


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL(db_path = "database/hotel_reservation_sample.db")

    def create_hotel(self, hotel_name: str, stars: int) -> None:
        self.__hotel_dal.create_hotel(hotel_name, stars)

    def update_hotel(self, hotel_id: model.Hotel) -> None:
        self.__hotel_dal.update_hotel(hotel_id)

    def delete_hotel(self, hotel_id: int) -> None:
        self.__hotel_dal.delete_hotel(hotel_id)

    def search_hotels_by_stars(self, stars: int) -> None:
        self.__hotel_dal.search_hotels_by_stars(stars)

    def search_hotels_by_name(self, name: str) -> None:
        self.__hotel_dal.search_hotels_by_name(name)

