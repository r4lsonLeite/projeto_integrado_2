from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


trilhas_namespace = Namespace("trilhas", description="Trilhas personalizadas de aprendizagem")

conteudo_output = trilhas_namespace.model(
    "ConteudoOutput",
    {
        "id": fields.Integer,
        "titulo": fields.String,
        "descricao": fields.String,
        "categoria": fields.String,
        "url": fields.String,
        "carga_horaria": fields.Integer,
    },
)

trilha_item_output = trilhas_namespace.model(
    "TrilhaItemOutput",
    {
        "ordem": fields.Integer,
        "obrigatorio": fields.Boolean,
        "conteudo": fields.Nested(conteudo_output),
    },
)

trilha_input = trilhas_namespace.model(
    "TrilhaInput",
    {
        "usuario_id": fields.Integer(required=True),
        "tipo": fields.String(required=True),
        "status": fields.String,
    },
)

trilha_output = trilhas_namespace.model(
    "TrilhaOutput",
    {
        "id": fields.Integer,
        "usuario_id": fields.Integer,
        "tipo": fields.String,
        "status": fields.String,
        "criado_em": fields.String,
        "itens": fields.List(fields.Nested(trilha_item_output)),
    },
)


@trilhas_namespace.route("")
class TrilhasListResource(Resource):
    @jwt_required()
    @trilhas_namespace.marshal_list_with(trilha_output)
    def get(self):
        data, status_code = container.trilha_controller.list_trilhas()
        return data, status_code

    @jwt_required()
    @trilhas_namespace.expect(trilha_input, validate=True)
    @trilhas_namespace.marshal_with(trilha_output, code=201)
    def post(self):
        payload = trilhas_namespace.payload
        try:
            return container.trilha_controller.create_trilha(payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404