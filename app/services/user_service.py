from app.repositories.sqlite import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def list_users(self) -> list[dict]:
        return [user.to_dict() for user in self.user_repository.list_all()]

    def get_user(self, user_id: int) -> dict:
        user = self.user_repository.get_by_id(user_id)
        if not user:
            raise LookupError("Usuária não encontrada.")
        return user.to_dict()