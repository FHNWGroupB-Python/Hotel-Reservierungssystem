import model
import data_access

class FacilityManager:
    def __init__(self):
        self.__facility_dal = data_access.FacilityDAL()

    def create_facility(self, facility: str) -> model.Facility:
        return self.__facility_dal.create_facility(facility)

    def update_facility(self, facility: model.Facility) -> None:
        self.__facility_dal.update_facility(facility)

    def delete_facility(self, facility: model.Facility) -> None:
        self.__facility_dal.delete_facility(facility)