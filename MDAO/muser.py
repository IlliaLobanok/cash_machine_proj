from IDAO import IUser_DAO
from entities import User
from typing import Union, Optional, List


class MUser_DAO(IUser_DAO):
    connection_manager = None

    @staticmethod
    def initialize(connection_manager):
        MUser_DAO.connection_manager = connection_manager

    @staticmethod
    def create_user(name: str, password: str, role_ID: int):
        connection = MUser_DAO.connection_manager.get_connection()
        query = f'INSERT INTO users (role_ID, user_name, user_password) ' \
                f'VALUES ({role_ID}, "{name}", "{password}");'
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
    def read_user(search_value: Union[str, int]) -> Union[User, None]:
        connection = MUser_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'SELECT * FROM users WHERE user_ID = {search_value};'
        else:
            query = f'SELECT * FROM users WHERE user_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        connection.close()
        if row is not None:
            found_user = User(*row)
            return found_user
        else:
            return None

    @staticmethod
    def read_all_user() -> List[User]:
        connection = MUser_DAO.connection_manager.get_connection()
        query = f'SELECT * FROM users;'
        cursor = connection.cursor(buffered=True)
        cursor.execute(query)
        products = [User(*i) for i in cursor.fetchall()]
        cursor.close()
        connection.close()
        return products

    @staticmethod
    def update_user(search_value: Union[str, int], n_name: Optional[str] = None,
                    n_password: Optional[str] = None, n_role_ID: Optional[int] = None):
        connection = MUser_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query_clause = f'WHERE user_ID = {search_value};'
        else:
            query_clause = f'WHERE user_name = "{search_value}";'
        query = 'UPDATE users SET '
        i = 0
        if n_name is not None:
            query_name = f'user_name = "{n_name}" '
            query += query_name
            i += 1
        if n_password is not None:
            query_password = f'user_password = {n_password} '
            if i > 0:
                query = query + ', ' + query_password
            else:
                query += query_password
            i += 1
        if n_role_ID is not None:
            query_role = f'role_ID = {n_role_ID} '
            if i > 0:
                query = query + ', ' + query_role
            else:
                query += query_role
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
    def delete_user(search_value: Union[str, int]):
        connection = MUser_DAO.connection_manager.get_connection()
        if isinstance(search_value, int):
            query = f'DELETE FROM users WHERE user_ID = {search_value};'
        else:
            query = f'DELETE FROM users WHERE user_name = "{search_value}";'
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            connection.commit()
        except Exception as e:
            print(f"MYSQL_Handled_Error: {e}")
        finally:
            cursor.close()
            connection.close()
