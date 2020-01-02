from decimal import Decimal
from dateutil.parser import parse


from bricklane_platform.models.card import Card
from bricklane_platform.config import PAYMENT_FEE_RATE


class Payment(object):

    customer_id = None
    date = None
    amount = None
    fee = None
    card_id = None

    def __init__(self, data=None):
        print(data)
        if "bank_account_id" in data:
            print("Bank...")
            id = "bank_account_id"
        elif "card_id" in data:
            id = "card_id"
            print("Card...")
        print("ID - , %s!" % id)
        print(data.get("bank_account_id"))


        if not data:
            return

        self.customer_id = int(data["customer_id"])
        self.date = parse(data["date"])

        total_amount = Decimal(data["amount"])
        self.fee = total_amount * PAYMENT_FEE_RATE
        self.amount = total_amount - self.fee

        card = Card()
        card.card_id = int(data["card_id"])
        card.status = data["card_status"]
        self.card = card

    def is_successful(self):
        return self.card.status == "processed"
