import model
import data_access

class HotelManager():
    def __init__(self) -> None:
        self.__hotel_dal = data_access.Hotel.DAL()

    def create_hotel(self, hotel_name:str, street:str, city:str, zip_code:int, country:str, stars:int, number_of_rooms:int) ->model.Hotel:
        return self.__hotel_dal.create_hotel(hotel_name, street, city, zip_code, country, stars, number_of_rooms)

