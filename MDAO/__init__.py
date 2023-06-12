from .mproduct import MProduct_DAO
from .mreceipt import MReceipt_DAO
from .mreceipt_product import MReceipt_Product_DAO
from .mrole import MRole_DAO
from .muser import MUser_DAO

from connection_manager import ConnectionManager
conn_manager = ConnectionManager()
MProduct_DAO.initialize(conn_manager)
MReceipt_DAO.initialize(conn_manager)
MReceipt_Product_DAO.initialize(conn_manager)
MRole_DAO.initialize(conn_manager)
MUser_DAO.initialize(conn_manager)
