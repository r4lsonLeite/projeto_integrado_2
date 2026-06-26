from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


finance_namespace = Namespace("financeiro", description="Cobranças e pagamentos")

invoice_input = finance_namespace.model(
    "InvoiceInput",
    {
        "order_id": fields.Integer(required=True),
        "amount": fields.Float(required=True),
        "due_date": fields.String(required=True),
        "client_id": fields.Integer(required=True),
        "status": fields.String,
        "issue_date": fields.String,
    },
)

invoice_output = finance_namespace.model(
    "InvoiceOutput",
    {
        "id": fields.Integer,
        "order_id": fields.Integer,
        "amount": fields.Float,
        "due_date": fields.String,
        "client_id": fields.Integer,
        "status": fields.String,
        "issue_date": fields.String,
    },
)

payment_input = finance_namespace.model(
    "PaymentInput",
    {
        "invoice_id": fields.Integer(required=True),
        "amount": fields.Float(required=True),
        "gateway_type": fields.String(required=True),
        "transaction_gateway": fields.String(required=True),
        "status": fields.String,
        "payment_date": fields.String,
        "confirmar": fields.Boolean,
    },
)

payment_output = finance_namespace.model(
    "PaymentOutput",
    {
        "id": fields.Integer,
        "invoice_id": fields.Integer,
        "amount": fields.Float,
        "gateway_type": fields.String,
        "transaction_gateway": fields.String,
        "status": fields.String,
        "payment_date": fields.String,
    },
)


@finance_namespace.route("/faturas")
class InvoicesResource(Resource):
    @jwt_required()
    @finance_namespace.marshal_list_with(invoice_output)
    def get(self):
        data, status_code = container.finance_controller.list_invoices()
        return data, status_code

    @jwt_required()
    @finance_namespace.expect(invoice_input, validate=True)
    @finance_namespace.marshal_with(invoice_output, code=201)
    def post(self):
        try:
            return container.finance_controller.create_invoice(finance_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@finance_namespace.route("/pagamentos")
class PaymentsResource(Resource):
    @jwt_required()
    @finance_namespace.marshal_list_with(payment_output)
    def get(self):
        data, status_code = container.finance_controller.list_payments()
        return data, status_code

    @jwt_required()
    @finance_namespace.expect(payment_input, validate=True)
    @finance_namespace.marshal_with(payment_output, code=201)
    def post(self):
        try:
            return container.finance_controller.create_payment(finance_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

@finance_namespace.route("/faturas/<int:invoice_id>")
class InvoiceDetailResource(Resource):
    @jwt_required()
    @finance_namespace.marshal_with(invoice_output)
    def get(self, invoice_id):
        try:
            data, status_code = container.finance_controller.get_invoice(invoice_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @finance_namespace.expect(invoice_input, validate=True)
    @finance_namespace.marshal_with(invoice_output, code=200)
    def put(self, invoice_id):
        try:
            return container.finance_controller.update_invoice(invoice_id, finance_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, invoice_id):
        try:
            return container.finance_controller.delete_invoice(invoice_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@finance_namespace.route("/pagamentos/<int:payment_id>")
class PaymentDetailResource(Resource):
    @jwt_required()
    @finance_namespace.marshal_with(payment_output)
    def get(self, payment_id):
        try:
            data, status_code = container.finance_controller.get_payment(payment_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @finance_namespace.expect(payment_input, validate=True)
    @finance_namespace.marshal_with(payment_output, code=200)
    def put(self, payment_id):
        try:
            return container.finance_controller.update_payment(payment_id, finance_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, payment_id):
        try:
            return container.finance_controller.delete_payment(payment_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404
