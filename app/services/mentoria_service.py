from app.models.mentoria import Mentoria
from app.repositories.sqlite import MentoriaRepository, UserRepository


class MentoriaService:
    def __init__(self, mentoria_repository: MentoriaRepository, user_repository: UserRepository) -> None:
        self.mentoria_repository = mentoria_repository
        self.user_repository = user_repository

    def list_mentorias(self) -> list[dict]:
        return [mentoria.to_dict() for mentoria in self.mentoria_repository.list_all()]

    def agendar(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["usuario_id"])
        if not user:
            raise LookupError("Usuária da mentoria não encontrada.")

        mentoria = Mentoria(
            usuario_id=payload["usuario_id"],
            mentora=payload["mentora"],
            data_hora=payload["data_hora"],
            tema=payload["tema"],
            observacoes=payload.get("observacoes"),
        )
        created_mentoria = self.mentoria_repository.create(mentoria)
        return created_mentoria.to_dict()