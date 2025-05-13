class AdditionalServiceManager:
    def __init__(self):
        self.__service_da = data_access.AdditionalServiceDataAccess()

    def create_service(self, name: str, price: float) -> model.AdditionalService:
        return self.__service_da.create_service(name, price)

    def update_service(self, service: model.AdditionalService) -> None:
        self.__service_da.update_service(service)

    def delete_service(self, service: model.AdditionalService) -> None:
        self.__service_da.delete_service(service)