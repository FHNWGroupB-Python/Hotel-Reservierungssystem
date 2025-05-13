class FacilityManager:
    def __init__(self):
        self.__facility_da = data_access.FacilityDataAccess()

    def create_facility(self, facility: str) -> model.Facility:
        return self.__facility_da.create_facility(facility)

    def update_facility(self, facility: model.Facility) -> None:
        self.__facility_da.update_facility(facility)

    def delete_facility(self, facility: model.Facility) -> None:
        self.__facility_da.delete_facility(facility)