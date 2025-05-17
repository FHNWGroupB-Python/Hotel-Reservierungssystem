from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:

    from model.hotel import Hotel

class Facility:
    def __init__(self, facilityid: int, facility: str):
        self.facilityid = facilityid
        self.facility = facility

    def __str__(self):
        return (f"Einrichtung: {self.facility}")