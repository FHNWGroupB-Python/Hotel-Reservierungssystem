from __future__ import annotations
import model
from data_access.base_dal import BaseDAL

class InvoiceDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Invoice(
        invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        status TEXT NOT NULL,
        invoice_date TEXT NOT NULL
        )
        """
        self.execute(sql)

    def create_invoice(self, booking_id:int, issue_date: str, total_amount: float) -> model.Invoice:
        sql = """
        INSERT INTO Invoice (booking_id, issue_date, total_amount) VALUES (?,?,?)
        """
        params = (
            booking_id,
            issue_date,
            total_amount
        )
        self.execute(sql, params)

