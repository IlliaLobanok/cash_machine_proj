from model.IDAO import IProduct_DAO
from model.entities import Product
from typing import Union, Optional, List


class MProduct_DAO(IProduct_DAO):
    connection_manager = None

    @staticmethod
    def initialize(connection_manager):
        MProduct_DAO.connection_manager = connection_manager

    @staticmethod
    def create_product(name: str, price: float, quantity: Optional[float] = 0.0):
        connection = MProduct_DAO.connection_manager.get_connection()
        query = f'INSERT INTO products (product_name, product_price, avl_quantity) ' \
                f'VALUES ("{name}", {price}, {quantity});'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def read_product(search_value: Union[str, int]) -> Union[Product, None]:
        connection = MProduct_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'SELECT * FROM products WHERE product_ID = {search_value};'
        else:
            query = f'SELECT * FROM products WHERE product_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            found_product = Product(*row)
            return found_product
        else:
            return None

    @staticmethod
    def read_all_product() -> List[Product]:
        connection = MProduct_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM products;'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        products = [Product(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return products

    @staticmethod
    def update_product(search_value: Union[str, int], n_name: Optional[str] = None,
                       n_price: Optional[float] = None, n_quantity: Optional[float] = None):
        connection = MProduct_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query_clause = f'WHERE product_ID = {search_value};'
        else:
            query_clause = f'WHERE product_name = "{search_value}";'
        query = 'UPDATE products SET '
        i = 0
        if n_name is not None:
            query_name = f'product_name = "{n_name}" '
            query += query_name
            i += 1
        if n_price is not None:
            query_price = f'product_price = {n_price} '
            if i > 0:
                query = query + ', ' + query_price
            else:
                query += query_price
            i += 1
        if n_quantity is not None:
            query_quantity = f'avl_quantity = {n_quantity} '
            if i > 0:
                query = query + ', ' + query_quantity
            else:
                query += query_quantity
            i += 1
        query += query_clause
        if i > 0:
            cursor = connection.cursor(buffered=True)
            try:
                cursor.execute(query)
                connection.commit()
            except Exception as e:
                print(f"MYSQL_Handled_Error: {e}")
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def delete_product(search_value: Union[str, int]):
        connection = MProduct_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'DELETE FROM products WHERE product_ID = {search_value};'
        else:
            query = f'DELETE FROM products WHERE product_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()
