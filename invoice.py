import datetime
class Invoice:
    def __init__(self, invoice_id: int, order_id: int, amount: float, due_date: datetime, client_id: int, status: str, issue_date: datetime):
        self.invoice_id = invoice_id
        self.order_id = order_id
        self.amount = amount
        self.due_date = due_date
        self.client_id = client_id
        self.status = status
        self.issue_date = issue_date
    def generate_charge(self):
        if self.status == 'pending':
            self.status = 'awaiting_payment'
            print(f"Invoice {self.invoice_id}: Charge generated successfully.")
            return True
        print(f"Invoice {self.invoice_id} is already being processed.")
        return False
    def register_payment_confirmed(self):
        self.status = 'paid'
        print(f"Invoice {self.invoice_id} updated: PAID.")
