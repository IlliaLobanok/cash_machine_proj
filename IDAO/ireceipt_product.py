from abc import ABC, abstractmethod
from typing import Union, Optional, List
from entities import ReceiptHasProduct


class IReceipt_Product_DAO(ABC):

    @staticmethod
    @abstractmethod
    def create_receipt_product(receipt_ID: int, product_ID: int, quantity: float):
        """
        insert new receipt-has-product relation
        :param receipt_ID: int;
        :param product_ID: int;
        :param quantity: float;
        """

    @staticmethod
    @abstractmethod
    def read_receipt_product(receipt_ID: int) -> List[ReceiptHasProduct]:
        """
        search receipt's products by its id
        :param receipt_ID: int;
        """

    @staticmethod
    @abstractmethod
    def read_all_receipt_product() -> List[ReceiptHasProduct]:
        """
        select all receipt-has-product relations
        """

    @staticmethod
    @abstractmethod
    def update_receipt_product(receipt_ID: int, product_ID: int, n_quantity: float):
        """
        update product's quantity in the receipt
        :param receipt_ID: int;
        :param product_ID: int;
        :param n_quantity: float;
        """

    @staticmethod
    @abstractmethod
    def delete_receipt_product(receipt_ID: int, product_ID: int):
        """
        delete receipt's product by their ids
        :param receipt_ID: int;
        :param product_ID: int;
        """