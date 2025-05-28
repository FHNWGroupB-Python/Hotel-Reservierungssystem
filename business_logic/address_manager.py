import model
import data_access

class AddressManager:
    def __init__(self):
        self.__address_dal = data_access.AddressDAL()

    def create_address(self, street: str, city: str, zip_code: int) -> model.Address:
        return self.__address_dal.create_address(street, city, zip_code)

    def update_address(self, address: model.Address) -> model.Address:
        return self.__address_dal.update_address(address)

    def delete_address(self, address: model.Address) -> model.Address:
        return self.__address_dal.delete_address(address)


