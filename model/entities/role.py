

class Role:
    def __init__(self, id: int, name: str):
        self._id = int(id)
        self._name = str(name)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_value: int):
        self._id = id_value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name_value: str):
        self._name = name_value
