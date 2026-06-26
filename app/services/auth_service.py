from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from app.models.user import User
from app.repositories.sqlite import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register(self, payload: dict) -> dict:
        if self.user_repository.get_by_email(payload["email"]):
            raise ValueError("E-mail já cadastrado.")

        user = User(
            nome=payload["nome"],
            email=payload["email"],
            senha_hash=generate_password_hash(payload["senha"]),
            telefone=payload.get("telefone"),
            endereco=payload.get("endereco"),
            papel=payload.get("papel", "empreendedora"),
        )
        created_user = self.user_repository.create(user)
        return created_user.to_dict()

    def login(self, email: str, senha: str) -> dict:
        user = self.user_repository.get_by_email(email)
        if not user or not user.check_password(senha):
            raise PermissionError("Credenciais inválidas.")

        token = create_access_token(
            identity=str(user.user_id),
            additional_claims={"papel": user.papel, "email": user.email},
        )
        return {"access_token": token, "usuario": user.to_dict()}

    def get_user_from_identity(self, identity: str) -> dict:
        user = self.user_repository.get_by_id(int(identity))
        if not user:
            raise LookupError("Usuária não encontrada.")
        return user.to_dict()