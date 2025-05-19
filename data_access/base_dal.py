import os
import sqlite3


class BaseDAL:
    def __init__(self, db_connection:str = None):
            if db_connection is None:
                self.db_connection_str = os.environ.get("hotel_reservation_db")
                if self.db_connection_str is None:
                    raise Exception("Database connection string not found")
            else:
                self.db_connection_str = db_connection


    def _connect(self):
        return sqlite3.connect(self.db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql:str,  params:tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                result = cursor.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return result

    def fetchall(self, sql:str, params:tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                results = cursor.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return results

    def execute(self, sql:str, params:tuple = None):
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
        return cursor.lastrowid, cursor.rowcount
