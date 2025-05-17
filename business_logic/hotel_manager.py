import model
import data_access

class HotelManager():
    def __init__(self) -> None:
        self.__hotel_dal = data_access.Hotel.DAL()

    def create_hotel(self, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int) ->model.Hotel:
        return self.__hotel_dal.create_hotel(hotel_name, street, city, zip_code, country, stars, number_of_rooms)

    def read_hotel(self) -> list[model.Hotel]:
        hotels_data = self.__hotel_dal.get_all_hotels()
        hotel_list = []

        for hotel_data in hotels_data:
            hotel = model.Hotel(
                hotel_id=hotel_data["hotel_id"],
                hotel_name=hotel_data["hotel_name"],
                street=hotel_data["street"],
                city=hotel_data["city"],
                zip_code=hotel_data["zip_code"],
                country=hotel_data["country"],
                stars=hotel_data["stars"],
                number_of_rooms=hotel_data["number_of_rooms"]
            )
            hotel_list.append(hotel)

        return hotel_list

    def search_hotels_by_city(self, city: str):
        return self.__hotel_dal.search_hotels_by_city(city)

    def search_hotels_by_stars(self, stars: int):
        return self.__hotel_dal.search_hotels_by_stars(stars)
