import mysql.connector
from singleton_decorator import singleton


@singleton
class ConnectionManager:
    def __init__(self):
        self.connection_pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="ConnectionManagerPool",
            host="127.0.0.1",
            user="root",
            password="",
            database="PIS_schema")

    def get_connection(self):
        return self.connection_pool.get_connection()