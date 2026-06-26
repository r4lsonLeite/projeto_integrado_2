from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Invoice:
    order_id: int
    amount: float
    due_date: str
    client_id: int
    status: str = "pending"
    issue_date: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    invoice_id: int | None = None

    def generate_charge(self) -> bool:
        if self.status != "pending":
            return False
        self.status = "awaiting_payment"
        return True

    def register_payment_confirmed(self) -> None:
        self.status = "paid"

    def to_dict(self) -> dict:
        return {
            "id": self.invoice_id,
            "order_id": self.order_id,
            "amount": self.amount,
            "due_date": self.due_date,
            "client_id": self.client_id,
            "status": self.status,
            "issue_date": self.issue_date,
        }


@dataclass(slots=True)
class Payment:
    invoice_id: int
    amount: float
    gateway_type: str
    transaction_gateway: str
    status: str = "pending"
    payment_date: str | None = None
    payment_id: int | None = None

    def process_and_confirm(self, confirmation_date: str, invoice_object: Invoice) -> bool:
        if self.status != "pending":
            return False
        self.status = "confirmed"
        self.payment_date = confirmation_date
        invoice_object.register_payment_confirmed()
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.payment_id,
            "invoice_id": self.invoice_id,
            "amount": self.amount,
            "gateway_type": self.gateway_type,
            "transaction_gateway": self.transaction_gateway,
            "status": self.status,
            "payment_date": self.payment_date,
        }