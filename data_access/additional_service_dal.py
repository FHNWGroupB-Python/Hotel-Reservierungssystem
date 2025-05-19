from __future__ import annotations

from data_access.base_dal import BaseDAL

class AdditionalServiceDAL(BaseDAL):
    def __init__(self, db_path:str = None):
        super().__init__(db_path)