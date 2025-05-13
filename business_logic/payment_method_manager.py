import model
import data_access

class PaymentMethodManager:
    def __init__(self):
        self.__payment_dal = data_access.PaymentMethodDAL()

    def create_payment_method(self, name: str) -> model.PaymentMethod:
        return self.__payment_dal.create_payment_method(name)

    def delete_payment_method(self, payment_method: model.PaymentMethod) -> None:
        self.__payment_dal.delete_payment_method(payment_method)
