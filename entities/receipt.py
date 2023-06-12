

class Receipt:
    def __init__(self, id: int, cashier_id: int, current_sum: float):
        self._id = int(id)
        self._cashier_id = int(cashier_id)
        self._current_sum = float(current_sum)

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id_value: int):
        self._id = id_value

    @property
    def cashier_id(self) -> int:
        return self._cashier_id

    @cashier_id.setter
    def cashier_id(self, cashier_id_value: int):
        self._cashier_id = cashier_id_value

    @property
    def current_sum(self) -> float:
        return self._current_sum

    @current_sum.setter
    def current_sum(self, current_sum_value: float):
        self._current_sum = current_sum_value
