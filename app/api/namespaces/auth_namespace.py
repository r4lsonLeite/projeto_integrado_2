from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


auth_namespace = Namespace("auth", description="Autenticação e sessão")

register_input = auth_namespace.model(
    "RegisterInput",
    {
        "nome": fields.String(required=True),
        "email": fields.String(required=True),
        "senha": fields.String(required=True),
        "telefone": fields.String,
        "endereco": fields.String,
        "papel": fields.String,
    },
)

login_input = auth_namespace.model(
    "LoginInput",
    {
        "email": fields.String(required=True),
        "senha": fields.String(required=True),
    },
)

user_output = auth_namespace.model(
    "UserOutput",
    {
        "id": fields.Integer,
        "nome": fields.String,
        "email": fields.String,
        "telefone": fields.String,
        "endereco": fields.String,
        "papel": fields.String,
        "ativo": fields.Boolean,
        "criado_em": fields.String,
    },
)

token_output = auth_namespace.model(
    "TokenOutput",
    {
        "access_token": fields.String,
        "usuario": fields.Nested(user_output),
    },
)


@auth_namespace.route("/register")
class RegisterResource(Resource):
    @auth_namespace.expect(register_input, validate=True)
    @auth_namespace.response(201, "Usuária criada", user_output)
    def post(self):
        payload = auth_namespace.payload
        try:
            return container.auth_controller.register(payload)
        except ValueError as exc:
            return {"message": str(exc)}, 400


@auth_namespace.route("/login")
class LoginResource(Resource):
    @auth_namespace.expect(login_input, validate=True)
    @auth_namespace.response(200, "Login realizado", token_output)
    def post(self):
        payload = auth_namespace.payload
        try:
            return container.auth_controller.login(payload)
        except PermissionError as exc:
            return {"message": str(exc)}, 401


@auth_namespace.route("/me")
class MeResource(Resource):
    @jwt_required()
    @auth_namespace.response(200, "Usuária autenticada", user_output)
    def get(self):
        return container.auth_controller.me(get_jwt_identity())