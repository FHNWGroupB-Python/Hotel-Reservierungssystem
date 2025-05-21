from __future__ import annotations

class Address:
    def __init__(self, address_id:int, street:str, city:str, zip_code:int):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        self.__customer = None
        self.__hotel = None

    @property
    def address_id(self):
        return self.__address_id

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        if not isinstance(street, str):
            raise ValueError("Street must be a string")
        if not street:
            raise ValueError("Street cannot be empty")
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise ValueError("City must be a string")
        if not city:
            raise ValueError("City cannot be empty")
        self.__city = city

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code: int):
        if not isinstance(zip_code, int):
            raise ValueError("zip_code must be an integer")
        self.__zip_code = zip_code