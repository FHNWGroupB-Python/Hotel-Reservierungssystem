class Invoice:
    def __init__(self, invoiceid:int, amount:str, status:str, invoice_date:str, booking: "Booking" = None):
        self.invoiceid = invoiceid
        self.amount = amount
        self.status = status
        self.invoice_date = invoice_date
        self.booking = booking # Referenz auf Booking 1-zu-1 Komposition

    def __str__(self):
        return (f"Invoice ID: {self.invoiceid}, Betrag: {self.amount}, status: {self.status}")
