import model
import data_access


class HotelManager:
    def __init__(self) -> None:
        self.__hotel_dal = data_access.HotelDAL()

    def create_hotel(self, hotel_name: str, street: str, city: str, zip_code: int, country: str, stars: int, number_of_rooms: int) -> model.Hotel:
        if not hotel_name or not isinstance(hotel_name, str):
            raise ValueError("Hotelname ist ungültig.")
        if not city or not isinstance(city, str):
            raise ValueError("Die Stadt darf nicht leer sein.")
        if stars < 1 or stars > 5:
            raise ValueError("Sterne müssen zwischen 1 und 5 liegen.")

        try:
            created_hotel = self.__hotel_dal.create_hotel(
                hotel_name, street, city, zip_code, country, stars, number_of_rooms
            )
            print(f"Hotel '{hotel_name}' wurde erfolgreich erstellt.")
            return created_hotel
        except Exception as e:
            print(f"Fehler beim Erstellen des Hotels: {e}")
            raise

    def search_hotels_by_city(self, city: str) -> list[model.Hotel]:
        try:
            if not city:
                raise ValueError("Bitte geben Sie eine Stadt ein.")
            return self.__hotel_dal.search_hotels_by_city(city)
        except Exception as e:
            print(f"Fehler bei der Suche nach Hotels in der Stadt '{city}': {e}")
            raise

    def search_hotels_by_stars(self, stars: int) -> list[model.Hotel]:
        try:
            if not isinstance(stars, int) or stars < 1 or stars > 5:
                raise ValueError("Die Anzahl der Sterne muss zwischen 1 und 5 liegen.")
            return self.__hotel_dal.search_hotels_by_stars(stars)
        except Exception as e:
            print(f"Fehler bei der Suche nach Hotels mit {stars} Sternen: {e}")
            raise
