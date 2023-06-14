from model.IDAO import IReceipt_DAO
from model.entities import Receipt
from typing import Union, Optional, List


class MReceipt_DAO(IReceipt_DAO):
    connection_manager = None

    @staticmethod
    def initialize(connection_manager):
        MReceipt_DAO.connection_manager = connection_manager

    @staticmethod
    def create_receipt(cashier_ID: int, current_sum: Optional[float] = 0.0) -> Optional[int]:
        connection = MReceipt_DAO.connection_manager.get_connection()
        query = f'INSERT INTO receipt (cashier_ID, receipt_sum) ' \
                f'VALUES ({cashier_ID}, {current_sum});'
        query_get_id = f'SELECT receipt_ID, cashier_ID, receipt_sum FROM receipt WHERE cashier_ID = {cashier_ID} ' \
                       f'ORDER BY receipt_time DESC LIMIT 1;'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
            cursor.execute(query_get_id)
            receipt = Receipt(*cursor.fetchone())
            receipt_ID = receipt.id
        except Exception as e:
            receipt_ID = None
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            return receipt_ID
            cursor.close()
            connection.close()

    @staticmethod
    def read_receipt(receipt_ID: int) -> Union[Receipt, None]:
        connection = MReceipt_DAO.connection_manager.get_connection()
        query = f'SELECT receipt_ID, cashier_ID, receipt_sum FROM receipt WHERE receipt_ID = {receipt_ID};'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            found_receipt = Receipt(*row)
            return found_receipt
        else:
            return None

    @staticmethod
    def read_all_receipt() -> List[Receipt]:
        connection = MReceipt_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM receipt;'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        receipts = [Receipt(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return receipts

    @staticmethod
    def update_receipt(receipt_ID: int, n_sum: float):
        connection = MReceipt_DAO.connection_manager.get_connection()
        query = f'UPDATE receipt SET receipt_sum = {n_sum} WHERE receipt_ID = {receipt_ID};'
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
    def delete_receipt(receipt_ID: int):
        connection = MReceipt_DAO.connection_manager.get_connection()
        query = f'DELETE FROM receipt WHERE receipt_ID = {receipt_ID};'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()
