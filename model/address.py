class Address:
    def __init__(self, adressid:int, street:str, zip_code:int, city:str, country:str):
        self.adressid = adressid
        self.street = street
        self.zip_code = zip_code
        self.city = city
        self.country = country

    def __str__(self):
        return (f"Adresse ID: {self.adressid}, street: {self.street}, zip_code: {self.zip_code}, city: {self.city}, country: {self.country}")
