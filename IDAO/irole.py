from abc import ABC, abstractmethod
from typing import Union, Optional, List
from entities import Role


class IRole_DAO(ABC):

    @staticmethod
    @abstractmethod
    def create_role(name: str):
        """
        insert new role
        :param name: str;
        """

    @staticmethod
    @abstractmethod
    def read_role(search_value: Union[str, int]) -> Union[Role, None]:
        """
        search roles by id and name
        :param search_value: int, str;
        """

    @staticmethod
    @abstractmethod
    def read_all_roles() -> List[Role]:
        """
        select all roles
        """

    @staticmethod
    @abstractmethod
    def update_role(search_value: Union[str, int], n_name: str):
        """
        update role's name
        :param search_value: int, str;
        :param n_name: str;
        """

    @staticmethod
    @abstractmethod
    def delete_role(search_value: Union[str, int]):
        """
        delete role by its name or id
        :param search_value: int, str;
        """