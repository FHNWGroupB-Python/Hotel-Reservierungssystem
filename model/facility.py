class Facilities:
    def __init__(self, facilityid: int, facility: str):
        self.facilityid = facilityid
        self.facility = facility

    def __str__(self):
        return (f"Einrichtung: {self.facility}")