from app.models.agenda import AgendaMentora
from app.models.avaliacao import AvaliacaoMentoria
from app.repositories.sqlite import MentorAgendaRepository, MentoriaRepository, MentoriaReviewRepository, UserRepository


class MentoringOpsService:
    def __init__(
        self,
        agenda_repository: MentorAgendaRepository,
        mentoria_repository: MentoriaRepository,
        review_repository: MentoriaReviewRepository,
        user_repository: UserRepository,
    ) -> None:
        self.agenda_repository = agenda_repository
        self.mentoria_repository = mentoria_repository
        self.review_repository = review_repository
        self.user_repository = user_repository

    def list_agendas(self) -> list[dict]:
        return [agenda.to_dict() for agenda in self.agenda_repository.list_all()]

    def create_agenda(self, payload: dict) -> dict:
        agenda = AgendaMentora(mentora_id=payload["mentora_id"], data_hora=payload["data_hora"], usuario_id=payload.get("usuario_id"), disponivel=payload.get("disponivel", True))
        created = self.agenda_repository.create(agenda)
        return created.to_dict()

    def list_reviews(self) -> list[dict]:
        return [review.to_dict() for review in self.review_repository.list_all()]

    def create_review(self, payload: dict) -> dict:
        mentoria = self.mentoria_repository.get_by_id(payload["mentoria_id"])
        if not mentoria:
            raise LookupError("Mentoria não encontrada para avaliação.")
        review = AvaliacaoMentoria(mentoria_id=payload["mentoria_id"], nota=float(payload["nota"]), comentario=payload["comentario"], data_avaliacao=payload.get("data_avaliacao"))
        created = self.review_repository.create(review)
        return created.to_dict()

    def get_agenda(self, agenda_id: int) -> dict:
        agenda = self.agenda_repository.get_by_id(agenda_id)
        if not agenda:
            raise LookupError("Agenda não encontrada.")
        return agenda.to_dict()

    def update_agenda(self, agenda_id: int, payload: dict) -> dict:
        agenda = self.agenda_repository.get_by_id(agenda_id)
        if not agenda:
            raise LookupError("Agenda não encontrada.")
        return agenda.to_dict()

    def delete_agenda(self, agenda_id: int) -> bool:
        agenda = self.agenda_repository.get_by_id(agenda_id)
        if not agenda:
            raise LookupError("Agenda não encontrada.")
        return True

    def get_review(self, review_id: int) -> dict:
        review = self.review_repository.get_by_id(review_id)
        if not review:
            raise LookupError("Avaliação não encontrada.")
        return review.to_dict()

    def update_review(self, review_id: int, payload: dict) -> dict:
        review = self.review_repository.get_by_id(review_id)
        if not review:
            raise LookupError("Avaliação não encontrada.")
        return review.to_dict()

    def delete_review(self, review_id: int) -> bool:
        review = self.review_repository.get_by_id(review_id)
        if not review:
            raise LookupError("Avaliação não encontrada.")
        return True