from __future__ import annotations

from data_access.base_dal import BaseDAL

class RoomDAL(BaseDAL):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Room(
        room_id INTEGER PRIMARY KEY AUTOINCREMENT,
        hotel_id INTEGER NOT NULL,
        room_type TEXT NOT NULL,
        max_guests INTEGER NOT NULL,
        description TEXT,
        price_per_night REAL NOT NULL,
        amenities TEXT)
        """
        self.execute(sql)

    def get_room_details_by_hotel(self, hotel_id: int) -> list[dict]:
        sql = """
        SELECT room_type, max_guests, description, price_per_night, amenities FROM Room WHERE hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel_id,))

        room_details = []
        for row in rows:
            room_details.append({
                "room_type": row[0],
                "max_guests": row[1],
                "description": row[2],
                "price_per_night": row[3],
                "amenities": row[4].split(", ") if row[4] else []
            })
        return room_details

    def create_room(self, hotel_id: int, room_type: str, max_guests: int, description: str, price_per_night: float,
                 amenities: list[str]) -> int:

        amenities_csv = ", ".join(amenities)
        sql = """
        INSERT INTO Room (hotel_id, room_type, max_guests, description, price_per_night, amenities) VALUES (?, ?, ?, ?, ?, ?)
        """
        room_id, _ = self.execute(sql, (hotel_id, room_type, max_guests, description, price_per_night, amenities_csv))
        return room_id

    def delete_room(self, room_id: int) -> None:
        sql = """
        DELETE FROM Room WHERE room_id = ?
        """
        self.execute(sql, (room_id,))

    def update_room(self, room_id: int, room_type: str = None, max_guests: int = None, description: str = None, price_per_night: float = None, amenities: list[str] = None) -> None:

        updates = []
        params = []

        if room_type:
            updates.append("room_type = ?")
            params.append(room_type)

        if max_guests:
            updates.append("max_guests = ?")
            params.append(max_guests)

        if description:
            updates.append("description = ?")
            params.append(description)

        if price_per_night:
            updates.append("price_per_night = ?")
            params.append(price_per_night)

        if amenities:
            amenities_csv = ", ".join(amenities)
            updates.append("amenities = ?")
            params.append(amenities_csv)

        # Es gibt nichts zu aktualisieren, wenn dies leer ist
        if not updates:
            raise ValueError("Es wurden keine Werte für das Update bereitgestellt.")

        params.append(room_id)

        sql = f"UPDATE Room SET {', '.join(updates)} WHERE room_id = ?"
        self.execute(sql, tuple(params))