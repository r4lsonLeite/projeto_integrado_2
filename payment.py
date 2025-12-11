class Payment:
    def __init__(self, payment_id, invoice_id, amount, gateway_type, transaction_gateway, status, payment_date):
        self.payment_id = payment_id
        self.invoice_id = invoice_id
        self.amount = amount
        self.gateway_type = gateway_type
        self.transaction_gateway = transaction_gateway
        self.status = status
        self.payment_date = payment_date
    def process_and_confirm(self, confirmation_date):
        if self.status == 'pending':
            print(f"Payment {self.payment_id}: Processing via {self.gateway_type}...")
            self.status = 'confirmed'
            self.payment_date = confirmation_date
            print("Payment confirmed and registered.")
            return True
            print(f"Payment {self.payment_id} could not be processed. Status: {self.status}.")
        return False



    