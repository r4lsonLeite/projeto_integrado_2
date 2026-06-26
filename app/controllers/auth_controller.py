from app.services.auth_service import AuthService


class AuthController:
    def __init__(self, auth_service: AuthService) -> None:
        self.auth_service = auth_service

    def register(self, payload: dict) -> tuple[dict, int]:
        user = self.auth_service.register(payload)
        return user, 201

    def login(self, payload: dict) -> tuple[dict, int]:
        token_data = self.auth_service.login(payload["email"], payload["senha"])
        return token_data, 200

    def me(self, identity: str) -> tuple[dict, int]:
        user = self.auth_service.get_user_from_identity(identity)
        return user, 200