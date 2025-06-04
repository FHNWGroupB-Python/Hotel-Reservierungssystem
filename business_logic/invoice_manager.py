import model
import data_access

class InvoiceManager:
    def __init__(self):
        self.__invoice_dal = data_access.InvoiceDAL(db_path = "database/hotel_reservation_sample.db")

    def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> model.Invoice:
        # Ensure booking_id is provided and valid
        if not isinstance(booking_id, int) or booking_id <= 0:
            raise ValueError("Invalid booking_id")

        # Ensure issue_date is a valid date
        if not isinstance(issue_date, str):
            raise ValueError("Invalid issue_date")
        return self.__invoice_dal.create_invoice(booking_id, issue_date, total_amount)

    def read_invoice(self) -> list[model.Invoice]:
        return self.__invoice_dal.read_invoice()

