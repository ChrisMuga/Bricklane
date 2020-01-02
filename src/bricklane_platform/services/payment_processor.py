import csv

from bricklane_platform.models.payment import Payment


class PaymentProcessor(object):

    def get_payments(self, csv_path, source):
        payments = []
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                payments.append(Payment(row))

        return payments

    def verify_payments(self, payments):
        successful_payments = []
        for payment in payments:
            if 'bank' in vars(payment):
                successful_payments.append(payment)
            elif payment.is_successful():
                successful_payments.append(payment)

        return successful_payments
