import model
import data_access

class FacilityManager:
    def __init__(self):
        self.__facility_dal = data_access.FacilityDAL(db_path = "database/hotel_reservation_sample.db")

    def create_facility(self, facility: model.Facility) -> model.Facility:
        return self.__facility_dal.create_facility(facility)

    def update_facility(self, faclity: model.Facility) -> model.Facility:
        return self.__facility_dal.update_facility(faclity)

    def delete_facility(self, facility: model.Facility) -> model.Facility:
        return self.__facility_dal.delete_facility(facility)

