class Invoice:
    
    def __init__(self, invoice_id, order_id, amount, due_date, client_id, status, issue_date):
        self.invoice_id = invoice_id
        self.order_id = order_id
        self.amount = amount
        self.due_date = due_date
        self.client_id = client_id
        self.status = status
        self.issue_date = issue_date
    def to_dict(self):
        return {
            'invoice_id': self.invoice_id,
            'order_id': self.order_id,
            'amount': self.amount,
            'due_date': self.due_date,
            'client_id': self.client_id,
            'status': self.status,
            'issue_date': self.issue_date
        }
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