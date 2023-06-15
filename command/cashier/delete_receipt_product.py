from command import Command
from model import MProduct_DAO, MReceipt_Product_DAO, update_current_sum, update_avl_quantity, find_receipt_product
from typing import Optional, Union


class DeleteReceiptProductCommand(Command):
    def __init__(self, receipt_id: int, product_value: Union[int, str]):
        self.receipt_id = receipt_id
        self.product_value = product_value

    def execute_command(self):
        found_product = MProduct_DAO.read_product(self.product_value)
        receipt_product = find_receipt_product(self.receipt_id, self.product_value)
        MReceipt_Product_DAO.delete_receipt_product(self.receipt_id, found_product.id)
        update_avl_quantity(found_product.id, -receipt_product.quantity)
        update_current_sum(self.receipt_id, found_product.id, -receipt_product.quantity)
