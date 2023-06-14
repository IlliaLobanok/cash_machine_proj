from model import MProduct_DAO, MReceipt_DAO, MReceipt_Product_DAO, MRole_DAO, MUser_DAO

# MProduct_DAO.update_product("груша", n_quantity=40.56)
products = MProduct_DAO.read_all_product()
for product in products:
    print(product.id, product.name, product.price, product.quantity)
peach = MProduct_DAO.read_product("груша")
apple = MProduct_DAO.read_product("яблуко")

MRole_DAO.create_role("cashier")
cashier_role = MRole_DAO.read_role("cashier")
print(cashier_role.id, cashier_role.name, "\n")

MUser_DAO.create_user("cashier1", "123456", cashier_role.id)
user_cashier1 = MUser_DAO.read_user("cashier1")
print(user_cashier1.id, user_cashier1.name, user_cashier1.password, user_cashier1.role_id, "\n")

receipt_id = MReceipt_DAO.create_receipt(user_cashier1.id)
if receipt_id is not None:
    MReceipt_Product_DAO.create_receipt_product(receipt_id, peach.id, 5)
    MReceipt_DAO.update_receipt(receipt_id, peach.price * 5)

    MReceipt_Product_DAO.create_receipt_product(receipt_id, apple.id, 2)
    receipt = MReceipt_DAO.read_receipt(receipt_id)
    MReceipt_DAO.update_receipt(receipt_id, receipt.current_sum + apple.price * 2)

    MReceipt_Product_DAO.update_receipt_product(receipt_id, apple.id, 2.5)
    receipt = MReceipt_DAO.read_receipt(receipt_id)
    MReceipt_DAO.update_receipt(receipt_id, receipt.current_sum + apple.price * 2.5)

    list_receipt_product = MReceipt_Product_DAO.read_receipt_product(receipt_id)
    for receipt_product in list_receipt_product:
        print(receipt_product.receipt_id, receipt_product.product_id, receipt_product.quantity)

    MProduct_DAO.update_product(peach.name, n_quantity=peach.quantity - 5)
    MProduct_DAO.update_product(apple.name, n_quantity=apple.quantity - 2.5)

    products = MProduct_DAO.read_all_product()
    for product in products:
        print(product.id, product.name, product.price, product.quantity)
else:
    print("receipt_id is None\n")
