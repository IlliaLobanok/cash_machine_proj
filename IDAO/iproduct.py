from abc import ABC, abstractmethod
from typing import Union, Optional, List
from entities import Product


class IProduct_DAO(ABC):

    @staticmethod
    @abstractmethod
    def create_product(name: str, price: float, quantity: Optional[float] = 0.0):
        """
        insert new product
        :param name: str;
        :param price: float;
        :param quantity: float;
        """

    @staticmethod
    @abstractmethod
    def read_product(search_value: Union[str, int]) -> Union[Product, None]:
        """
        search products by id and name
        :param search_value: int, str;
        """

    @staticmethod
    @abstractmethod
    def read_all_product() -> List[Product]:
        """
        select all products
        """

    @staticmethod
    @abstractmethod
    def update_product(search_value: Union[str, int], n_name: Optional[str] = None,
                       n_price: Optional[float] = None, n_quantity: Optional[float] = None):
        """
        update product's fields that are mentioned
        :param search_value: int, str;
        :param n_name: str;
        :param n_price: int;
        :param n_quantity: int;
        """

    @staticmethod
    @abstractmethod
    def delete_product(search_value: Union[str, int]):
        """
        delete product by its name or id
        :param search_value: int, str;
        """
