from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


partners_namespace = Namespace("parcerias", description="Parceiros e ofertas institucionais")

partner_input = partners_namespace.model(
    "PartnerInput",
    {
        "name": fields.String(required=True),
        "partner_type": fields.String(required=True),
        "contact": fields.String(required=True),
    },
)

partner_output = partners_namespace.model(
    "PartnerOutput",
    {
        "id": fields.Integer,
        "name": fields.String,
        "partner_type": fields.String,
        "contact": fields.String,
    },
)

offer_input = partners_namespace.model(
    "PartnerOfferInput",
    {
        "partner_id": fields.Integer(required=True),
        "title": fields.String(required=True),
        "description": fields.String(required=True),
        "criteria_json": fields.String(required=True),
        "enrollment_url": fields.String(required=True),
        "is_active": fields.Boolean,
    },
)

offer_output = partners_namespace.model(
    "PartnerOfferOutput",
    {
        "id": fields.Integer,
        "partner_id": fields.Integer,
        "title": fields.String,
        "description": fields.String,
        "criteria_json": fields.String,
        "enrollment_url": fields.String,
        "is_active": fields.Boolean,
    },
)


@partners_namespace.route("/parceiros")
class PartnersResource(Resource):
    @partners_namespace.marshal_list_with(partner_output)
    def get(self):
        data, status_code = container.partner_controller.list_partners()
        return data, status_code

    @jwt_required()
    @partners_namespace.expect(partner_input, validate=True)
    @partners_namespace.marshal_with(partner_output, code=201)
    def post(self):
        return container.partner_controller.create_partner(partners_namespace.payload)


@partners_namespace.route("/parceiros/<int:partner_id>")
class PartnerDetailResource(Resource):
    @partners_namespace.marshal_with(partner_output)
    def get(self, partner_id):
        try:
            data, status_code = container.partner_controller.get_partner(partner_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @partners_namespace.expect(partner_input, validate=True)
    @partners_namespace.marshal_with(partner_output, code=200)
    def put(self, partner_id):
        try:
            return container.partner_controller.update_partner(partner_id, partners_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, partner_id):
        try:
            return container.partner_controller.delete_partner(partner_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@partners_namespace.route("/ofertas/<int:offer_id>")
class OfferDetailResource(Resource):
    @partners_namespace.marshal_with(offer_output)
    def get(self, offer_id):
        try:
            data, status_code = container.partner_controller.get_offer(offer_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @partners_namespace.expect(offer_input, validate=True)
    @partners_namespace.marshal_with(offer_output, code=200)
    def put(self, offer_id):
        try:
            return container.partner_controller.update_offer(offer_id, partners_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, offer_id):
        try:
            return container.partner_controller.delete_offer(offer_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404