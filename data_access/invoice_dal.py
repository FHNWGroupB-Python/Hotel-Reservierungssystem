from __future__ import annotations

from data_access.base_dal import BaseDAL

class InvoiceDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)


def create_invoice(self, amount: float, status: str, invoice_date: date) -> model.Invoice:
    if amount is None or amount <= 0:
        raise ValueError("Amount must be a positive number.")
    if not status or not isinstance(status, str):
        raise ValueError("Status must be a non-empty string.")
    if not isinstance(invoice_date, date):
        raise ValueError("invoice_date must be a valid date object.")

    sql = """
        INSERT INTO Invoice (amount, status, invoice_date)
        VALUES (?, ?, ?)
        """
    params = (amount, status, invoice_date.isoformat())
    last_row_id, _ = self.execute_sql(sql, params)

    return model.Invoice(invoice_id=last_row_id, amount=amount, status=status, invoice_date=invoice_date)


def update_invoice(self, invoice: model.Invoice) -> None:
    if not invoice or not invoice.invoice_id:
        raise ValueError("Invoice must have a valid ID for update.")

    sql = """
        UPDATE Invoice
        SET amount = ?, status = ?, invoice_date = ?
        WHERE invoice_id = ?
        """
    params = (
        invoice.amount,
        invoice.status,
        invoice.invoice_date.isoformat(),
        invoice.invoice_id
    )
    self.execute_sql(sql, params)


def delete_invoice(self, invoice_id: int) -> None:
    if not invoice_id or invoice_id <= 0:
        raise ValueError("A valid invoice ID is required.")

    sql = "DELETE FROM Invoice WHERE invoice_id = ?"
    self.execute_sql(sql, (invoice_id,))


def read_invoice_by_id(self, invoice_id: int) -> model.Invoice | None:
    if not invoice_id or invoice_id <= 0:
        raise ValueError("A valid invoice ID is required.")

    sql = "SELECT invoice_id, amount, status, invoice_date FROM Invoice WHERE invoice_id = ?"
    result = self.fetchone(sql, (invoice_id,))

    if result:
        invoice_id, amount, status, invoice_date = result
        return model.Invoice(invoice_id=invoice_id, amount=amount, status=status,
                             invoice_date=date.fromisoformat(invoice_date))
    return None


def read_all_invoices(self) -> list[model.Invoice]:
    sql = "SELECT invoice_id, amount, status, invoice_date FROM Invoice"
    rows = self.fetchall(sql)

    return [
        model.Invoice(
            invoice_id=row[0],
            amount=row[1],
            status=row[2],
            invoice_date=date.fromisoformat(row[3])
        )
        for row in rows
    ]


def search_invoices_by_status(self, status: str) -> list[model.Invoice]:
    if not status or not isinstance(status, str):
        raise ValueError("Status must be a non-empty string.")

    sql = """
        SELECT invoice_id, amount, status, invoice_date
        FROM Invoice
        WHERE status = ?
        """
    rows = self.fetchall(sql, (status,))

    return [
        model.Invoice(
            invoice_id=row[0],
            amount=row[1],
            status=row[2],
            invoice_date=date.fromisoformat(row[3])
        )
        for row in rows
    ]