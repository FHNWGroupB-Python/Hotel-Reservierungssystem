from __future__ import annotations

import model
from data_access.base_dal import BaseDAL

class FacilityDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)

    def create_facility(self, facility: model.Facility) -> model.Facility:
        sql = """
        INSERT INTO Facility (facility_name) VALUES (?)
        """
        params = (
            facility.facility_name,
        )
        self.execute(sql, params)

    def update_facility(self, facility: model.Facility) -> model.Facility:
        sql = """
        UPDATE Facility SET facility_name = ? WHERE facility_id = ?
        """
        params = (
            facility.facility_name,
        )
        self.execute(sql, params)

    def delete_facility(self, facility: model.Facility) -> model.Facility:
        sql = """
        DELETE FROM Facility WHERE facility_id = ?
        """
        params = (
            facility.facility_id,
        )
        self.execute(sql, params)
