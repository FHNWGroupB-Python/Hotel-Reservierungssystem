import model
import data_access

from data_access.review_dal import ReviewDAL
from model.review import Review

class ReviewManager:
    def __init__(self) -> None:
        self.__review_dal = data_access.ReviewDAL()

    def get_reviews_by_hotel(self, hotel_id: int) -> list[Review]:
        return self.__review_dal.get_reviews_by_hotel(hotel_id)

    def create_review(self, hotel_id: int, guest_id: int, rating: int, comment: str) -> Review:
        if not (1 <= rating <= 5):
            raise ValueError("Rating muss zwischen 1 und 5 liegen.")
        return self.__review_dal.create_review(hotel_id, guest_id, rating, comment)

