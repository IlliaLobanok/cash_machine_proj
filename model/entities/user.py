

class User:
    def __init__(self, id: int, role_id: int, name: str, password: str):
        self._id = int(id)
        self._role_id = int(role_id)
        self._name = str(name)
        self._password = str(password)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, user_id_value: int):
        self._id = user_id_value

    @property
    def role_id(self) -> int:
        return self._role_id

    @role_id.setter
    def role_id(self, role_id_value: int):
        self._role_id = role_id_value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_value: str):
        self._name = name_value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password_value: str):
        self._password = password_value
