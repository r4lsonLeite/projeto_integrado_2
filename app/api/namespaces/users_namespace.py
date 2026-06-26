from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


users_namespace = Namespace("usuarios", description="Gestão de usuárias")

user_output = users_namespace.model(
    "UsuariosOutput",
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


@users_namespace.route("")
class UsersListResource(Resource):
    @jwt_required()
    @users_namespace.marshal_list_with(user_output)
    def get(self):
        data, status_code = container.user_controller.list_users()
        return data, status_code


@users_namespace.route("/<int:user_id>")
class UserDetailResource(Resource):
    @jwt_required()
    @users_namespace.marshal_with(user_output)
    def get(self, user_id: int):
        try:
            return container.user_controller.get_user(user_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404