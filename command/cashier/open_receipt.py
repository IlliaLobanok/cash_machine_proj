from command import Command
from model import MReceipt_DAO
from typing import Optional


class OpenReceiptCommand(Command):
    def __init__(self, user_id:int):
        self.user_id = user_id

    def execute_command(self) -> Optional[int]:
        receipt_id = MReceipt_DAO.create_receipt(self.user_id)
        return receipt_id
