from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


orders_namespace = Namespace("pedidos", description="Pedidos do marketplace")

order_item_input = orders_namespace.model(
    "OrderItemInput",
    {
        "produto_id": fields.Integer(required=True),
        "quantidade": fields.Integer(required=True),
    },
)

order_item_output = orders_namespace.model(
    "OrderItemOutput",
    {
        "produto_id": fields.Integer,
        "quantidade": fields.Integer,
        "preco_unitario": fields.Float,
        "total": fields.Float,
    },
)

order_input = orders_namespace.model(
    "OrderInput",
    {
        "usuario_id": fields.Integer(required=True),
        "endereco_entrega": fields.String(required=True),
        "itens": fields.List(fields.Nested(order_item_input), required=True),
    },
)

order_output = orders_namespace.model(
    "OrderOutput",
    {
        "id": fields.Integer,
        "usuario_id": fields.Integer,
        "endereco_entrega": fields.String,
        "status": fields.String,
        "data_criacao": fields.String,
        "valor_total": fields.Float,
        "itens": fields.List(fields.Nested(order_item_output)),
    },
)


@orders_namespace.route("")
class OrdersListResource(Resource):
    @jwt_required()
    @orders_namespace.marshal_list_with(order_output)
    def get(self):
        data, status_code = container.order_controller.list_orders()
        return data, status_code

    @jwt_required()
    @orders_namespace.expect(order_input, validate=True)
    @orders_namespace.marshal_with(order_output, code=201)
    def post(self):
        payload = orders_namespace.payload
        try:
            return container.order_controller.create_order(payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404