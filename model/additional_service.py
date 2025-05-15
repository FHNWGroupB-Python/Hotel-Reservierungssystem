from __future__ import annotations

class AdditionalService:
    def __init__(self, additionalserviceid, additional_service, additional_service_price):
        self.additionalserviceid = additionalserviceid
        self.additional_service = additional_service
        self.additional_service_price = additional_service_price

    def __str__(self):
        return (', '.join(f'{key}: {value}' for key, value in vars(self).items()))