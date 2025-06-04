import model
import data_access


class GuestManager:
    def __init__(self):
        self.__guest_dal = data_access.GuestDAL()

    def create_guest(self, guest: model.Guest) -> None:
        self.__guest_dal.create_guest(guest)

    def update_guest(self, guest: model.Guest) -> None:
        self.__guest_dal.update_guest(guest)

    def delete_guest(self, guest: model.Guest) -> None:
        self.__guest_dal.delete_guest(guest)
