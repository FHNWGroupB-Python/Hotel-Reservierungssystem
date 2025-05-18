from __future__ import annotations

class Facility:
    def __init__(self, facilityid: int, facility: str):
        self.__facilityid = facilityid
        self.__facility = facility

    @property
    def facilityid(self):
        return self.__facilityid

    @property
    def facility(self):
        return self.__facility
