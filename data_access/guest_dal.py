from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class GuestDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_guest(self, guest: model.Guest) -> None:
        sql = """
        INSERT INTO Guest (first_name, last_name, email) VALUES (?, ?, ?)
        """
        params = (
            guest.first_name,
            guest.last_name,
            guest.email
        )
        self.execute(sql, params)

    def update_guest(self, guest: model.Guest) -> None:
        sql = """
        UPDATE Guest SET first_name = ?, last_name = ?, email = ? WHERE guestid = ?
        """
        params = tuple([
            guest.first_name,
            guest.last_name,
            guest.email
        ]
        )
        self.execute(sql, params)

    def delete_guest(self, guest_id: int) -> None:
        sql = """
        DELETE FROM Guest WHERE guestid = ?
        """
        params = tuple([guest_id])
        self.execute(sql, params)

    def show_guest(self) -> list[model.Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email FROM Guest
        """
        rows = self.fetchall(sql)

        guests: list[model.Guest] = []
        for guest_id, first_name, last_name, email in rows:
            guests.append(model.Guest(guest_id, first_name, last_name, email))
        return guests


