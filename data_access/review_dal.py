from data_access.base_dal import BaseDAL
from model.review import Review
from model.hotel  import Hotel
from model.guest  import Guest

class ReviewDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)
        self.initialize_table()

    def initialize_table(self):
        sql = """
              CREATE TABLE IF NOT EXISTS Review(
              review_id INTEGER PRIMARY KEY AUTOINCREMENT,
              hotel_id INTEGER NOT NULL,
              guest_id INTEGER NOT NULL,
              rating INTEGER NOT NULL,
              comment TEXT NOT NULL,
              review_date DATE NOT NULL
              )
              """
        self.execute(sql)

    def get_reviews_by_hotel(self, hotel_id: int) -> list[Review]:
        sql = """
        SELECT
            r.review_id,
            r.guest_id,
            g.first_name,
            g.last_name,
            r.rating,
            r.comment,
            r.review_date
        FROM Review AS r
        JOIN Guest  AS g ON r.guest_id = g.guest_id
        WHERE r.hotel_id = ?
        ORDER BY r.review_date DESC
        """
        rows = self.fetchall(sql, (hotel_id,))

        reviews: list[Review] = []
        for review_id, guest_id, first_name, last_name, rating, comment, review_date in rows:
            # Hotel-Objekt nur mit ID (weitere Daten nicht nötig)
            hotel = Hotel(hotel_id, "", 0)
            guest = Guest(guest_id, first_name, last_name, "")
            rev   = Review(
                review_id,
                hotel,
                guest,
                rating,
                comment,
                review_date
            )
            reviews.append(rev)
        return reviews

    def create_review(self, hotel_id: int, guest_id: int, rating: int, comment: str) -> Review:
        sql = """
        INSERT INTO Review (hotel_id, guest_id, rating, comment, review_date)
        VALUES (?, ?, ?, ?, DATE('now'))
        """
        params = (
            hotel_id,
            guest_id,
            rating,
            comment,
        )
        lastrowid, _ = self.execute(sql, params)
        return self.get_review_by_id(lastrowid)

    def get_review_by_id(self, review_id: int) -> Review:
        sql = """
        SELECT hotel_id, guest_id, rating, comment, review_date
        FROM Review WHERE review_id = ?
        """
        row = self.fetchone(sql, (review_id,))
        hotel_id, guest_id, rating, comment, review_date = row
        hotel = Hotel(hotel_id, "", 0)
        guest = Guest(guest_id, "", "", "")
        return Review(review_id, hotel, guest, rating, comment, review_date)