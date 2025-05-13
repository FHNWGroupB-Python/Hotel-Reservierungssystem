import model
import data_access

class RoomManager:
    def __init__(self):
        self.__room_dal = data_access.RoomDAL()

    def create_room(self, hotel: model.Hotel, room_number: int, room_type: str, price: float) -> model.Room:
        return self.__room_dal.create_room(hotel, room_number, room_type, price)

    def update_room(self, room: model.Room) -> None:
        self.__room_dal.update_room(room)

    def delete_room(self, room: model.Room) -> None:
        self.__room_dal.delete_room(room)

    def check_availability(self, hotel: model.Hotel, check_in: str, check_out: str) -> list[model.Room]:
        return self.__room_dal.search_room_availability(hotel, check_in, check_out)

    def show_room_details(self, hotel_id: int) -> list[dict]:
        """
        Zeigt Details zu verschiedenen Zimmertypen eines Hotels an.

        :param hotel_id: Die ID des Hotels, dessen Zimmerdetails angezeigt werden sollen.
        :return: Eine Liste von Dictionaries, die die Details zu jedem Zimmertyp enthalten.
        """
        # Zimmerdetails aus der Datenbank abrufen (Simulation hier, tatsächliche Implementierung z.B. über DAL)
        room_data = self.__hotel_dal.get_room_details_by_hotel(hotel_id)

        # Ergebnisse prüfen
        if not room_data:
            raise ValueError(f"No room details found for Hotel ID {hotel_id}.")

        # Liste für Zimmerdetails vorbereiten
        room_details = []

        for room in room_data:
            details = {
                "room_type": room["room_type"],  # Zimmertyp (Single, Double, Suite, ...)
                "max_guests": room["max_guests"],  # Maximale Gästeanzahl
                "description": room["description"],  # Beschreibung des Zimmers
                "price_per_night": room["price_per_night"],  # Preis pro Nacht
                "amenities": room["amenities"],  # Ausstattungsliste (z. B. WLAN, TV, Minibar, ...)
            }
            room_details.append(details)

        return room_details

    def calculate_dynamic_price(self, base_price: float, season_factor: float = 1.0, demand_factor: float = 1.0, discount: float = 0.0) -> float:
        """
        Berechnet den dynamischen Preis basierend auf verschiedenen Faktoren.

        :param base_price: Grundpreis für eine Übernachtung.
        :param season_factor: Faktor basierend auf der Saison (z.B. Hauptsaison = 1.5, Nebensaison = 0.8).
        :param demand_factor: Faktor basierend auf der Nachfrage (z.B. hohe Nachfrage = 1.2).
        :param discount: Rabatt auf den finalen Preis (als absolute Zahl, z. B. 10 für 10CHF Rabatt).
        :return: Der berechnete dynamische Preis (float).
        """
        # Eingangswerte prüfen
        if base_price < 0:
            raise ValueError("Base price cannot be negative.")

        if discount < 0:
            raise ValueError("Discount cannot be negative.")

        # Dynamischen Preis berechnen
        dynamic_price = base_price * season_factor * demand_factor

        # Rabatt anwenden
        dynamic_price -= discount

        # Sicherstellen, dass der endgültige Preis nicht negativ ist
        return max(dynamic_price, 0)  # Rückgabe mindestens 0CHF