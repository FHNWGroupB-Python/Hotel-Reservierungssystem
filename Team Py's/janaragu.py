class address:
    def __init__(self, street:str, zip_code:int, city:str, country:str):
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def get_address(self):
        return f"street: {self.street}, zip_code: {self.zip_code}, city: {self.city}, country: {self.country}"

class customer:
    def __init__(self, first_name:str, last_name:str, phone:str, email:str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def get_customer_details(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, phone: {self.phone}, email: {self.email}"

class invoice:
    def __init__(self, amount:str, status:str, invoice_date:str):
        self.amount = amount
        self.status = status
        self.invoice_date = invoice_date

    def get_status(self):
        return f"status: {self.status}"

    def get_amount(self):
        return f"amount: {self.amount}"
