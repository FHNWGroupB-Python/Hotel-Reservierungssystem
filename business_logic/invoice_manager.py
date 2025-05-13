import model
import data_access

class InvoiceManager:
    def __init__(self):
        self.__invoice_dal = data_access.InvoiceDAL()

    def create_invoice(self, amount: float, invoice_date: str) -> model.Invoice:
        return self.__invoice_dal.create_invoice(amount, "offen", invoice_date)

    def delete_invoice(self, invoice: model.Invoice) -> None:
        self.__invoice_dal.delete_invoice(invoice)

    def show_invoice_details(self, invoice: model.Invoice) -> str:
        return invoice.get_details()