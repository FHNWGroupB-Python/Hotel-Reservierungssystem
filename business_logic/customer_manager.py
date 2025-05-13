import model
import data_access


class CustomerManager:
    def __init__(self):
        self.__customer_da = data_access.CustomerDataAccess()

    def create_customer(self, first_name: str, last_name: str, phone: str, email: str) -> model.Customer:
        return self.__customer_da.create_customer(first_name, last_name, phone, email)

    def update_customer(self, customer: model.Customer) -> None:
        self.__customer_da.update_customer(customer)

    def delete_customer(self, customer: model.Customer) -> None:
        self.__customer_da.delete_customer(customer)
