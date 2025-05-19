from __future__ import annotations

from data_access.base_dal import BaseDAL

class PaymentMethodDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)


 def create_payment_method(self, payment_method: str) -> model.PaymentMethod:
        if not payment_method or not isinstance(payment_method, str):
            raise ValueError("Payment method must be a non-empty string.")

        sql = """
        INSERT INTO PaymentMethod (payment_method)
        VALUES (?)
        """
        params = (payment_method,)
        last_row_id, _ = self.execute_sql(sql, params)

        return model.PaymentMethod(payment_method_id=last_row_id, payment_method=payment_method)

    def update_payment_method(self, method: model.PaymentMethod) -> None:
        if not method or not method.payment_method_id:
            raise ValueError("Valid PaymentMethod object with ID is required.")

        sql = """
        UPDATE PaymentMethod
        SET payment_method = ?
        WHERE payment_method_id = ?
        """
        params = (method.payment_method, method.payment_method_id)
        self.execute_sql(sql, params)

    def delete_payment_method(self, method_id: int) -> None:
        if not method_id or method_id <= 0:
            raise ValueError("Valid payment method ID is required.")

        sql = "DELETE FROM PaymentMethod WHERE payment_method_id = ?"
        self.execute_sql(sql, (method_id,))