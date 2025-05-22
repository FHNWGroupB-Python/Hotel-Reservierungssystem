import model
import data_access

class RoomTypeManager:
    def __init__(self):
        self.__room_type_dal = data_access.RoomTypeDAL(db_path = "database/")

