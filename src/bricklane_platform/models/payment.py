from decimal import Decimal
from dateutil.parser import parse

from bricklane_platform.models.bank import Bank
from bricklane_platform.models.card import Card
from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None
    id_key = None
    bank_account_id = None

    def __init__(self, data=None):
        
        if not data:
            return
        self.process_trx(data)
        

    def is_successful(self):
        if 'bank' not in vars(self):
            return self.card.status == "processed"
        
    def process_trx(self, data):
        self.customer_id = int(data.get("customer_id"))
        self.date = parse(data["date"])
        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee
        
        if "bank_account_id" in data:
            id_key = "bank_account_id"
            bank = Bank()
            bank.bank_account_id = int(data[id_key])
            bank.status = 'success'
            self.bank = bank
        elif "card_id" in data:
            id_key = "card_id"
            card = Card()
            card.card_id = int(data.get(id_key))
            card.status = data["card_status"]
            self.card = card