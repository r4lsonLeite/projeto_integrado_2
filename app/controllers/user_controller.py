from app.services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service

    def list_users(self) -> tuple[list[dict], int]:
        return self.user_service.list_users(), 200

    def get_user(self, user_id: int) -> tuple[dict, int]:
        return self.user_service.get_user(user_id), 200