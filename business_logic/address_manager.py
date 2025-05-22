import model
import data_access

class AddressManager:
    def __init__(self):
        self.__address_dal = data_access.AddressDAL(db_path = "database/")

    def create_address(self, address: model.Address) -> model.Address:
        return self.__address_dal.create_address(address)

    def update_address(self, address: model.Address) -> model.Address:
        return self.__address_dal.update_address(address)

    def delete_address(self, address: model.Address) -> model.Address:
        return self.__address_dal.delete_address(address)


