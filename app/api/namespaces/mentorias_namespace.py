from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


mentorias_namespace = Namespace("mentorias", description="Agendamentos e sessões")

mentoria_input = mentorias_namespace.model(
    "MentoriaInput",
    {
        "usuario_id": fields.Integer(required=True),
        "mentora": fields.String(required=True),
        "data_hora": fields.String(required=True),
        "tema": fields.String(required=True),
        "observacoes": fields.String,
    },
)

mentoria_output = mentorias_namespace.model(
    "MentoriaOutput",
    {
        "id": fields.Integer,
        "usuario_id": fields.Integer,
        "mentora": fields.String,
        "data_hora": fields.String,
        "tema": fields.String,
        "observacoes": fields.String,
        "status": fields.String,
        "criado_em": fields.String,
    },
)


@mentorias_namespace.route("")
class MentoriasListResource(Resource):
    @jwt_required()
    @mentorias_namespace.marshal_list_with(mentoria_output)
    def get(self):
        data, status_code = container.mentoria_controller.list_mentorias()
        return data, status_code

    @jwt_required()
    @mentorias_namespace.expect(mentoria_input, validate=True)
    @mentorias_namespace.marshal_with(mentoria_output, code=201)
    def post(self):
        payload = mentorias_namespace.payload
        try:
            return container.mentoria_controller.agendar(payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404