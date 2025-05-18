from __future__ import annotations

class AdditionalService:
    def __init__(self, additionalserviceid, additional_service, additional_service_price):
        self.__additionalserviceid = additionalserviceid
        self.__additional_service = additional_service
        self.__additional_service_price = additional_service_price

    @property
    def additionalserviceid(self):
        return self.__additionalserviceid

    @property
    def additional_service(self):
        return self.__additional_service

    @property
    def additional_service_price(self):
        return self.__additional_service_price

    @additional_service.setter
    def additional_service(self, additional_service):
        self.__additional_service = additional_service

