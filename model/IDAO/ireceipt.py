from abc import ABC, abstractmethod
from typing import Union, Optional, List
from model.entities import Receipt


class IReceipt_DAO(ABC):

    @staticmethod
    @abstractmethod
    def create_receipt(cashier_ID: int, current_sum: Optional[float] = 0.0) -> Optional[int]:
        """
        inserting new receipt
        :param cashier_ID: int;
        :param current_sum: float;
        """

    @staticmethod
    @abstractmethod
    def read_receipt(receipt_ID: int) -> Union[Receipt, None]:
        """
        search receipts by id
        :param receipt_ID: int;
        """

    @staticmethod
    @abstractmethod
    def read_all_receipt() -> List[Receipt]:
        """
        select all receipts
        """

    @staticmethod
    @abstractmethod
    def update_receipt(receipt_ID: int, n_sum: float):
        """
        update receipt's current sum
        :param receipt_ID: int;
        :param n_sum: float;
        """

    @staticmethod
    @abstractmethod
    def delete_receipt(receipt_ID: int):
        """
        delete receipt by its id
        :param receipt_ID: int;
        """
