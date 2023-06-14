

class ReceiptHasProduct:
    def __init__(self, receipt_id: int, product_id: int, quantity: float):
        self._receipt_id = int(receipt_id)
        self._product_id = int(product_id)
        self._quantity = float(quantity)

    @property
    def receipt_id(self) -> int:
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id_value: int):
        self._receipt_id = receipt_id_value

    @property
    def product_id(self) -> int:
        return self._product_id

    @product_id.setter
    def product_id(self, product_id_value: int):
        self._product_id = product_id_value

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity_value: float):
        self._quantity = quantity_value
