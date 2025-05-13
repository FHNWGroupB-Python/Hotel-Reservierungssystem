class PaymentMethodManager:
    def __init__(self):
        self.__payment_da = data_access.PaymentMethodDataAccess()

    def create_payment_method(self, name: str) -> model.PaymentMethod:
        return self.__payment_da.create_payment_method(name)

    def delete_payment_method(self, payment_method: model.PaymentMethod) -> None:
        self.__payment_da.delete_payment_method(payment_method)
