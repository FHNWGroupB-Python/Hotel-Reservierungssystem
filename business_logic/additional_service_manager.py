import model
import data_access

class AdditionalServiceManager:
    def __init__(self):
        self.__service_dal = data_access.AdditionalServiceDAL()

    def create_service(self, name: str, price: float) -> model.AdditionalService:
        return self.__service_dal.create_service(name, price)

    def update_service(self, service: model.AdditionalService) -> None:
        self.__service_dal.update_service(service)

    def delete_service(self, service: model.AdditionalService) -> None:
        self.__service_dal.delete_service(service)