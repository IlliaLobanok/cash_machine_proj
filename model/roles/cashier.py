from typing import Optional, Union, List
from model import *


class Cashier(Role):
    @staticmethod
    def open_receipt(user_id: int) -> Optional[int]:
        receipt_id = MReceipt_DAO.create_receipt(user_id)
        return receipt_id

    @staticmethod
    def add_receipt_product(receipt_id: int, product_value: Union[int, str], quantity: float):
        found_product = MProduct_DAO.read_product(product_value)
        if found_product.quantity < quantity:
            print(f"\nError: not enough product {found_product.name}\n")
            return None
        update_avl_quantity(found_product.id, quantity)
        MReceipt_Product_DAO.create_receipt_product(receipt_id, found_product.id, quantity)
        update_current_sum(receipt_id, found_product.id, quantity)

    @staticmethod
    def edit_receipt_product(receipt_id: int, product_value: Union[int, str], n_quantity: float):
        found_product = MProduct_DAO.read_product(product_value)
        if found_product.quantity < n_quantity:
            print(f"\nError: not enough product {found_product.name}\n")
            return None
        old_receipt_product = find_receipt_product(receipt_id, found_product.id)
        if old_receipt_product is None:
            print(f"\nError: there is no {found_product.name} in this receipt\n")
            return None
        update_avl_quantity(found_product.id, n_quantity - old_receipt_product.quantity)
        MReceipt_Product_DAO.update_receipt_product(receipt_id, found_product.id, n_quantity)
        update_current_sum(receipt_id, found_product.id, n_quantity - old_receipt_product.quantity)

    @staticmethod
    def remove_receipt_product(receipt_id: int, product_value: Union[int, str]):
        found_product = MProduct_DAO.read_product(product_value)
        receipt_product = find_receipt_product(receipt_id, product_value)
        MReceipt_Product_DAO.delete_receipt_product(receipt_id, found_product.id)
        update_avl_quantity(found_product.id, -receipt_product.quantity)
        update_current_sum(receipt_id, found_product.id, -receipt_product.quantity)
