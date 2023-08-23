from ..command import Command
from .delete_receipt_product import DeleteReceiptProductCommand
from model import MProduct_DAO, MReceipt_Product_DAO, update_current_sum, update_avl_quantity, find_receipt_product
from typing import Optional, Union


class EditReceiptProductCommand(Command):
    def __init__(self, receipt_id: int, product_value: Union[int, str], n_quantity: float):
        self.receipt_id = receipt_id
        self.product_value = product_value
        self.n_quantity = n_quantity

    def execute_command(self):
        found_product = MProduct_DAO.read_product(self.product_value)
        if found_product.quantity < self.n_quantity:
            print(f"\nError: not enough product {found_product.name}\n")
            return None
        old_receipt_product = find_receipt_product(self.receipt_id, found_product.id)
        if old_receipt_product is None:
            print(f"\nError: there is no {found_product.name} in this receipt\n")
            return None
        if self.n_quantity == 0.0:
            delete_command = DeleteReceiptProductCommand(self.receipt_id, self.product_value)
            delete_command.execute_command()
        else:
            update_avl_quantity(found_product.id, self.n_quantity - old_receipt_product.quantity)
            MReceipt_Product_DAO.update_receipt_product(self.receipt_id, found_product.id, self.n_quantity)
            update_current_sum(self.receipt_id, found_product.id, self.n_quantity - old_receipt_product.quantity)

