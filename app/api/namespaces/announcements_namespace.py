from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


announcements_namespace = Namespace("anuncios", description="Publicação de produtos no marketplace")

announcement_input = announcements_namespace.model(
    "AnnouncementInput",
    {
        "produto_id": fields.Integer(required=True),
        "data_publicacao": fields.String,
    },
)

announcement_output = announcements_namespace.model(
    "AnnouncementOutput",
    {
        "id": fields.Integer,
        "produto_id": fields.Integer,
        "status_anuncio": fields.String,
        "data_publicacao": fields.String,
    },
)


@announcements_namespace.route("/<int:anuncio_id>")
class AnnouncementDetailResource(Resource):
    @announcements_namespace.marshal_with(announcement_output)
    def get(self, anuncio_id):
        try:
            data, status_code = container.announcement_controller.get_announcement(anuncio_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @announcements_namespace.expect(announcement_input, validate=True)
    @announcements_namespace.marshal_with(announcement_output, code=200)
    def put(self, anuncio_id):
        try:
            return container.announcement_controller.update_announcement(anuncio_id, announcements_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, anuncio_id):
        try:
            return container.announcement_controller.delete_announcement(anuncio_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404