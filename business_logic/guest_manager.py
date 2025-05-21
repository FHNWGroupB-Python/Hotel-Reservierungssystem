import model
import data_access


class GuestManager:
    def __init__(self):
        self.__guest_dal = data_access.GuestDAL()

    def create_guest(self, first_name: str, last_name: str, email: str) -> None:
        self.__guest_dal.create_guest(first_name, last_name, email)

    def update_guest(self, guest: model.Guest) -> None:
        self.__guest_dal.update_guest(guest)

    def delete_guest(self, guest: model.Guest) -> None:
        self.__guest_dal.delete_guest(guest)
