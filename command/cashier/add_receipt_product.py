from ..command import Command
from .edit_receipt_product import EditReceiptProductCommand
from model import MProduct_DAO, MReceipt_Product_DAO, update_current_sum, update_avl_quantity
from typing import Optional, Union


class AddReceiptProductCommand(Command):
    def __init__(self, receipt_id: int, product_value: Union[int, str], quantity: float):
        self.receipt_id = receipt_id
        self.product_value = product_value
        self.quantity = quantity

    def execute_command(self):
        found_product = MProduct_DAO.read_product(self.product_value)
        if found_product.quantity < self.quantity:
            print(f"\nError: not enough product {found_product.name}\n")
            return None
        found_receipt_product = MReceipt_Product_DAO.read_receipt_product(self.receipt_id)
        if found_receipt_product is not None:
            for receipt_product in found_receipt_product:
                if receipt_product.product_id == found_product.id:
                    edit_command = EditReceiptProductCommand(self.receipt_id, self.product_value,
                                                             self.quantity + receipt_product.quantity)
                    print(f"\nProduct {found_product.name} already exists in the receipt. Updating quantity.\n")
                    edit_command.execute_command()
                    return None
        update_avl_quantity(found_product.id, self.quantity)
        MReceipt_Product_DAO.create_receipt_product(self.receipt_id, found_product.id, self.quantity)
        update_current_sum(self.receipt_id, found_product.id, self.quantity)

