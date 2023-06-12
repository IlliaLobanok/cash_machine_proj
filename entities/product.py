

class Product:
    def __init__(self, id: int, name: str, price: float, quantity: float):
        self._id = int(id)
        self._name = str(name)
        self._price = float(price)
        self._quantity = float(quantity)

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

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price_value: float):
        self._price = price_value

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity_value: float):
        self._quantity = quantity_value
