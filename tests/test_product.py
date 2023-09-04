from model.entities import Product
from model.MDAO import MProduct_DAO


def test_product():
    c_product1 = Product(id=1, name="тест1", price=99.99, quantity=100)
    c_product2 = Product(id=-1, name="тест2", price=50.50, quantity=50)
    u_product = Product(id=-1, name="тест3", price=30, quantity=40)

    try:
        MProduct_DAO.delete_product(c_product1.id)
        MProduct_DAO.delete_product(c_product2.name)
        MProduct_DAO.delete_product(u_product.name)
    finally:
        MProduct_DAO.create_product(c_product1.name, c_product1.price, c_product1.quantity, c_product1.id)
        MProduct_DAO.create_product(c_product2.name, c_product2.price, c_product2.quantity)

    assert MProduct_DAO.read_product(c_product1.id) is not None
    assert MProduct_DAO.read_product(c_product2.name) is not None

    r_product1 = MProduct_DAO.read_product(c_product1.id)
    r_product2 = MProduct_DAO.read_product(c_product2.name)

    assert r_product1 == c_product1
    assert r_product2 == c_product2

    MProduct_DAO.delete_product(c_product1.id)
    assert MProduct_DAO.read_product(c_product1.id) is None

    MProduct_DAO.update_product(c_product2.name, u_product.name, u_product.price, u_product.quantity)
    assert MProduct_DAO.read_product(u_product.name) == u_product
    assert MProduct_DAO.read_product(c_product2.name) is None

    MProduct_DAO.delete_product(u_product.name)
    assert MProduct_DAO.read_product(u_product.name) is None
