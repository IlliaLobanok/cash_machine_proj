from entities import *
from MDAO import *
from typing import Optional


def update_avl_quantity(product_id: int, quantity_decrement: float):
    found_product = MProduct_DAO.read_product(product_id)
    if found_product.quantity < quantity_decrement:
        print(f"\nError: not enough {found_product.name}\n")
        return None
    MProduct_DAO.update_product(found_product.id, n_quantity=found_product.quantity - quantity_decrement)


def update_current_sum(receipt_id: int, product_id: int, quantity_increment: float):
    found_product = MProduct_DAO.read_product(product_id)
    old_receipt = MReceipt_DAO.read_receipt(receipt_id)
    MReceipt_DAO.update_receipt(receipt_id, old_receipt.current_sum + found_product.price * quantity_increment)


def find_receipt_product(receipt_id: int, product_id: int) -> Optional[ReceiptHasProduct]:
    receipt_products = MReceipt_Product_DAO.read_receipt_product(receipt_id)
    for receipt_product in receipt_products:
        if receipt_product.product_id == product_id:
            return receipt_product
    return None
