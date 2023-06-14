from model.IDAO import IRole_DAO
from model.entities import Role
from typing import Union, List


class MRole_DAO(IRole_DAO):
    connection_manager = None

    @staticmethod
    def initialize(connection_manager):
        MRole_DAO.connection_manager = connection_manager

    @staticmethod
    def create_role(name: str):
        connection = MRole_DAO.connection_manager.get_connection()
        query = f'INSERT INTO roles (role_name) ' \
                f'VALUES ("{name}");'
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
    def read_role(search_value: Union[str, int]) -> Union[Role, None]:
        connection = MRole_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'SELECT * FROM roles WHERE role_ID = {search_value};'
        else:
            query = f'SELECT * FROM roles WHERE role_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            found_role = Role(*row)
            return found_role
        else:
            return None

    @staticmethod
    def read_all_roles() -> List[Role]:
        connection = MRole_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM roles;'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        roles = [Role(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return roles


    @staticmethod
    def update_role(search_value: Union[str, int], n_name: str):
        connection = MRole_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'UPDATE roles SET role_name = "{n_name}" WHERE role_ID = {search_value};'
        else:
            query = f'UPDATE roles SET role_name = "{n_name}" WHERE role_name = "{search_value}";'
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
    def delete_role(search_value: Union[str, int]):
        connection = MRole_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'DELETE FROM roles WHERE role_ID = {search_value};'
        else:
            query = f'DELETE FROM roles WHERE role_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()