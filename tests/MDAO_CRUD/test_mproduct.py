import pytest
from tests import create_connection
from model.entities import Product
from model.MDAO import MProduct_DAO
from tests import t_product1, t_product2, t_product3


@pytest.fixture
def check_remains(create_connection):
    query = f'DELETE FROM products WHERE product_ID = {t_product1.id} OR product_name = "{t_product2.name}";'
    test_conn = create_connection.get_connection()
    cursor = test_conn.cursor(buffered=True)
    try:
        cursor.execute(query)
        test_conn.commit()
    except Exception as e:
        print(f"MYSQL_Handled_Error: {e}")
    finally:
        cursor.close()
        test_conn.close()
        return True


def test_mproduct_create(check_remains, create_connection):
    if not check_remains:
        pytest.skip("There are still non-reverted remains of previous similar test in the database.")

    test_conn = create_connection.get_connection()

    MProduct_DAO.create_product(t_product1.name, t_product1.price, t_product1.quantity, t_product1.id)
    MProduct_DAO.create_product(t_product2.name, t_product2.price, t_product2.quantity)

    query1 = f'SELECT * FROM products WHERE product_ID = {t_product1.id};'
    query2 = f'SELECT * FROM products WHERE product_name = "{t_product2.name}";'

    cursor = test_conn.cursor(buffered=True)
    cursor.execute(query1)
    row = cursor.fetchone()
    if row is not None:
        found_product1 = Product(*row)
    else:
        pytest.skip("t_product1 was not retrieved from the database.")

    cursor.execute(query2)
    row = cursor.fetchone()
    if row is not None:
        found_product2 = Product(*row)
    else:
        pytest.skip("t_product2 was not retrieved from the database.")

    cursor.close()
    test_conn.close()

    assert found_product1 == t_product1
    assert found_product2 == t_product2


def test_mproduct_read():
    raise NotImplementedError


def test_mproduct_update():
    raise NotImplementedError


def test_mproduct_delete():
    raise NotImplementedError
