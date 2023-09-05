import mysql.connector
from connection_manager import ConnectionManager


def test_connection():
    test_conn = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="ConnectionManagerPool",
        host="127.0.0.1",
        user="root",
        password="",
        database="PIS_schema")
    connection = test_conn.get_connection()
    assert connection.is_connected() is True
    connection.close()


def test_connection_manager():
    connection_manager = ConnectionManager()
    connection = connection_manager.get_connection()
    assert connection.is_connected() is True
    connection.close()
