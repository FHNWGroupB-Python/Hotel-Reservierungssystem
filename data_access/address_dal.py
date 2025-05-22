from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class AddressDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Address(
        address_id INTEGER PRIMARY KEY AUTOINCREMENT,
        street TEXT NOT NULL,
        city TEXT NOT NULL,
        zip_code INTEGER NOT NULL
        )
        """
        self.execute(sql)

    def create_address(self, street: str, city: str, zip_code: int) -> model.Address:
        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?,?,?))
        """
        params = (
            street,
            city,
            zip_code
        )
        self.execute(sql, params)

    def update_address(self, address: model.Address):
        sql = """
        UPDATE Address SET street = ?, city = ?, zip_code = ? WHERE address_id = ?
        """
        params = tuple([
            address.street,
            address.city,
            address.zip_code,
            address.address_id
        ])
        self.execute(sql, params)

    def delete_address(self, address_id: int):
        sql = """
        DELETE FROM Address WHERE address_id = ?
        """
        params = tuple([address_id])
        self.execute(sql, params)
