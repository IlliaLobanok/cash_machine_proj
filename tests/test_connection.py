from connection_manager import ConnectionManager


def test_connection():
    connection_manager = ConnectionManager()
    connection = connection_manager.get_connection()
    assert connection.is_connected() is True
    connection.close()
