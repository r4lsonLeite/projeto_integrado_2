from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


products_namespace = Namespace("produtos", description="Marketplace e catálogo")

product_input = products_namespace.model(
    "ProductInput",
    {
        "usuario_id": fields.Integer(required=True),
        "titulo": fields.String(required=True),
        "descricao": fields.String(required=True),
        "valor": fields.Float(required=True),
        "categoria": fields.String(required=True),
        "status": fields.String,
    },
)

product_output = products_namespace.model(
    "ProductOutput",
    {
        "id": fields.Integer,
        "usuario_id": fields.Integer,
        "titulo": fields.String,
        "descricao": fields.String,
        "valor": fields.Float,
        "categoria": fields.String,
        "status": fields.String,
    },
)


@products_namespace.route("")
class ProductsListResource(Resource):
    @products_namespace.marshal_list_with(product_output)
    def get(self):
        data, status_code = container.product_controller.list_products()
        return data, status_code

    @jwt_required()
    @products_namespace.expect(product_input, validate=True)
    @products_namespace.marshal_with(product_output, code=201)
    def post(self):
        payload = products_namespace.payload
        try:
            return container.product_controller.create_product(payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404