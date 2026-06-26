from app.services.finance_service import FinanceService


class FinanceController:
    def __init__(self, finance_service: FinanceService) -> None:
        self.finance_service = finance_service

    def list_invoices(self) -> tuple[list[dict], int]:
        return self.finance_service.list_invoices(), 200

    def create_invoice(self, payload: dict) -> tuple[dict, int]:
        return self.finance_service.create_invoice(payload), 201

    def list_payments(self) -> tuple[list[dict], int]:
        return self.finance_service.list_payments(), 200

    def create_payment(self, payload: dict) -> tuple[dict, int]:
        return self.finance_service.create_payment(payload), 201

    def get_invoice(self, invoice_id: int) -> tuple[dict, int]:
        return self.finance_service.get_invoice(invoice_id), 200

    def update_invoice(self, invoice_id: int, payload: dict) -> tuple[dict, int]:
        return self.finance_service.update_invoice(invoice_id, payload), 200

    def delete_invoice(self, invoice_id: int) -> tuple[dict, int]:
        self.finance_service.delete_invoice(invoice_id)
        return {"message": "Fatura removida com sucesso"}, 204

    def get_payment(self, payment_id: int) -> tuple[dict, int]:
        return self.finance_service.get_payment(payment_id), 200

    def update_payment(self, payment_id: int, payload: dict) -> tuple[dict, int]:
        return self.finance_service.update_payment(payment_id, payload), 200

    def delete_payment(self, payment_id: int) -> tuple[dict, int]:
        self.finance_service.delete_payment(payment_id)
        return {"message": "Pagamento removido com sucesso"}, 204