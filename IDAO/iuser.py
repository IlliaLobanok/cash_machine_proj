from abc import ABC, abstractmethod
from typing import Union, Optional


class IUser_DAO(ABC):

    @staticmethod
    @abstractmethod
    def create_user(name: str, password: str, role_ID: int):
        """
        insert new user
        :param name: str;
        :param password: str;
        :param role_ID: int;
        """

    @staticmethod
    @abstractmethod
    def read_user(search_value: Union[str, int]):
        """
        search users by id and name
        :param search_value: int, str;
        """

    @staticmethod
    @abstractmethod
    def read_all_user():
        """
        select all users
        """

    @staticmethod
    @abstractmethod
    def update_user(search_value: Union[str, int], n_name: Optional[str] = None,
                    n_password: Optional[str] = None, n_role_ID: Optional[int] = None):
        """
        update user's fields that are mentioned
        :param search_value: int, str;
        :param n_name: str;
        :param n_password: str;
        :param n_role_ID: int;
        """

    @staticmethod
    @abstractmethod
    def delete_user(search_value: Union[str, int]):
        """
        delete user by its name or id
        :param search_value: int, str;
        """