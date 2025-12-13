import datetime

from projeto_integrado_2.invoice import Invoice
class Payment:
    def __init__(self, payment_id: int, invoice_id: int, amount:float, gateway_type: str, transaction_gateway: str, status: str, payment_date: datetime):
        self.payment_id = payment_id
        self.invoice_id = invoice_id
        self.amount = amount
        self.gateway_type = gateway_type
        self.transaction_gateway = transaction_gateway
        self.status = status
        self.payment_date = payment_date
    def process_and_confirm(self, confirmation_date: datetime, invoice_object: Invoice) -> bool:
        if self.status == 'pending':
            print(f"Payment {self.payment_id}: Processing via {self.gateway_type}...")
            self.status = 'confirmed'
            self.payment_date = confirmation_date
            invoice_object.register_payment_confirmed()
            print("Payment confirmed and registered.")
            return True
        print(f"Payment {self.payment_id} could not be processed. Status: {self.status}.")
        return False
