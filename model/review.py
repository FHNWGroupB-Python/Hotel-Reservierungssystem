from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.guest import Guest

class Review:
    def __init__(self, review_id:   int, hotel: Hotel, guest: Guest, rating: int, comment: str, review_date: date):
        self.__review_id = review_id
        self.hotel = hotel
        self.guest = guest
        self.rating = rating
        self.comment = comment
        self.review_date = review_date

    @property
    def review_id(self) -> int:
        return self.__review_id