from IDAO import IReceipt_Product_DAO
from entities import ReceiptHasProduct
from typing import Union, Optional, List


class MReceipt_Product_DAO(IReceipt_Product_DAO):
    connection_manager = None

    @staticmethod
    def initialize(connection_manager):
        MReceipt_Product_DAO.connection_manager = connection_manager

    @staticmethod
    def create_receipt_product(receipt_ID: int, product_ID: int, quantity: float):
        connection = MReceipt_Product_DAO.connection_manager.get_connection()
        query = f'INSERT INTO receipt_has_products (receipt_receipt_ID, products_product_ID, product_quantity) ' \
                f'VALUES ({receipt_ID}, {product_ID}, {quantity});'
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
    def read_receipt_product(receipt_ID: int) -> List[ReceiptHasProduct]:
        connection = MReceipt_Product_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM receipt_has_products WHERE receipt_receipt_ID = {receipt_ID};'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        found_receipt_product = [ReceiptHasProduct(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return found_receipt_product

    @staticmethod
    def read_all_receipt_product() -> List[ReceiptHasProduct]:
        connection = MReceipt_Product_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM receipt_has_products;'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        receipt_products = [ReceiptHasProduct(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return receipt_products

    @staticmethod
    def update_receipt_product(receipt_ID: int, product_ID: int, n_quantity: float):
        connection = MReceipt_Product_DAO.connection_manager.get_connection()
        query = f'UPDATE receipt_has_products SET product_quantity = {n_quantity} ' \
                f'WHERE receipt_receipt_ID = {receipt_ID} AND products_product_ID = {product_ID};'
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
    def delete_receipt_product(receipt_ID: int, product_ID: int):
        connection = MReceipt_Product_DAO.connection_manager.get_connection()
        query = f'DELETE FROM receipt_has_products WHERE receipt_receipt_ID = {receipt_ID} AND products_product_ID = {product_ID};'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()
