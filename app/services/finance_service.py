from app.models.financeiro import Invoice, Payment
from app.repositories.sqlite import InvoiceRepository, OrderRepository, PaymentRepository, UserRepository


class FinanceService:
    def __init__(
        self,
        invoice_repository: InvoiceRepository,
        payment_repository: PaymentRepository,
        order_repository: OrderRepository,
        user_repository: UserRepository,
    ) -> None:
        self.invoice_repository = invoice_repository
        self.payment_repository = payment_repository
        self.order_repository = order_repository
        self.user_repository = user_repository

    def list_invoices(self) -> list[dict]:
        return [invoice.to_dict() for invoice in self.invoice_repository.list_all()]

    def create_invoice(self, payload: dict) -> dict:
        order = self.order_repository.get_by_id(payload["order_id"])
        user = self.user_repository.get_by_id(payload["client_id"])
        if not order:
            raise LookupError("Pedido não encontrado para gerar fatura.")
        if not user:
            raise LookupError("Cliente da fatura não encontrado.")
        invoice = Invoice(order_id=payload["order_id"], amount=float(payload["amount"]), due_date=payload["due_date"], client_id=payload["client_id"], status=payload.get("status", "pending"), issue_date=payload.get("issue_date") or order.data_criacao)
        invoice.generate_charge()
        created = self.invoice_repository.create(invoice)
        return created.to_dict()

    def list_payments(self) -> list[dict]:
        return [payment.to_dict() for payment in self.payment_repository.list_all()]

    def create_payment(self, payload: dict) -> dict:
        invoice = self.invoice_repository.get_by_id(payload["invoice_id"])
        if not invoice:
            raise LookupError("Fatura não encontrada para pagamento.")
        payment = Payment(invoice_id=payload["invoice_id"], amount=float(payload["amount"]), gateway_type=payload["gateway_type"], transaction_gateway=payload["transaction_gateway"], status=payload.get("status", "pending"), payment_date=payload.get("payment_date"))
        if payload.get("confirmar", True):
            payment.process_and_confirm(payload.get("payment_date") or invoice.issue_date, invoice)
            self.invoice_repository.update_status(invoice.invoice_id, invoice.status)
        created = self.payment_repository.create(payment)
        return created.to_dict()

    def get_invoice(self, invoice_id: int) -> dict:
        invoice = self.invoice_repository.get_by_id(invoice_id)
        if not invoice:
            raise LookupError("Fatura não encontrada.")
        return invoice.to_dict()

    def update_invoice(self, invoice_id: int, payload: dict) -> dict:
        invoice = self.invoice_repository.get_by_id(invoice_id)
        if not invoice:
            raise LookupError("Fatura não encontrada.")
        return invoice.to_dict()

    def delete_invoice(self, invoice_id: int) -> bool:
        raise LookupError("Remoção de faturas não permitida.")

    def get_payment(self, payment_id: int) -> dict:
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            raise LookupError("Pagamento não encontrado.")
        return payment.to_dict()

    def update_payment(self, payment_id: int, payload: dict) -> dict:
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            raise LookupError("Pagamento não encontrado.")
        return payment.to_dict()

    def delete_payment(self, payment_id: int) -> bool:
        payment = self.payment_repository.get_by_id(payment_id)
        if not payment:
            raise LookupError("Pagamento não encontrado.")
        return True