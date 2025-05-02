class invoice:
    def __init__(self, invoiceid:int, amount:str, status:str, invoice_date:str):
        self.invoiceid = invoiceid
        self.amount = amount
        self.status = status
        self.invoice_date = invoice_date

    def __str__(self):
        return (f"Invoice ID: {self.invoiceid}, Betrag: {self.amount}, status: {self.status}")
