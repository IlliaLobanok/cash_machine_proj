import pytest
import mysql.connector
from model.entities import Product


@pytest.fixture(scope="session")
def create_connection():
    test_conn = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="TestConnectionPool",
        host="127.0.0.1",
        user="root",
        password="",
        database="PIS_schema")
    return test_conn


t_product1 = Product(id=1, name="тест1", price=99.99, quantity=100)
t_product2 = Product(id=-1, name="тест2", price=50.50, quantity=50)
t_product3 = Product(id=-1, name="тест3", price=30, quantity=40)
