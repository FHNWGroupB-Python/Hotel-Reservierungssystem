from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.hotel import Hotel
    from model.guest import Guest

class Review:
    def __init__(self, review_id:   int, hotel: Hotel, guest: Guest, rating: int, comment: str, review_date: date):
        self.__review_id = review_id
        self.__hotel = hotel
        self.__guest = guest
        self.__rating = rating
        self.__comment = comment
        self.__review_date = review_date

    @property
    def review_id(self) -> int:
        return self.__review_id

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def comment(self) -> str:
        return self.__comment

    @property
    def review_date(self) -> date:
        return self.__review_date