import model
import data_access

class InvoiceManager:
    def __init__(self):
        self.__invoice_dal = data_access.InvoiceDAL(db_path = "database/hotel_reservation_sample.db")

    def create_invoice(self, issue_date: str, total_amount: float) -> model.Invoice:
        self.__invoice_dal.create_invoice(issue_date, total_amount)

    def read_invoice(self) -> list[model.Invoice]:
        return self.__invoice_dal.read_invoice()


