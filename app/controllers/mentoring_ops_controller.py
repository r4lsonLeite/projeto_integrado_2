from app.services.mentoring_ops_service import MentoringOpsService


class MentoringOpsController:
    def __init__(self, mentoring_ops_service: MentoringOpsService) -> None:
        self.mentoring_ops_service = mentoring_ops_service

    def list_agendas(self) -> tuple[list[dict], int]:
        return self.mentoring_ops_service.list_agendas(), 200

    def create_agenda(self, payload: dict) -> tuple[dict, int]:
        return self.mentoring_ops_service.create_agenda(payload), 201

    def list_reviews(self) -> tuple[list[dict], int]:
        return self.mentoring_ops_service.list_reviews(), 200

    def create_review(self, payload: dict) -> tuple[dict, int]:
        return self.mentoring_ops_service.create_review(payload), 201

    def get_agenda(self, agenda_id: int) -> tuple[dict, int]:
        return self.mentoring_ops_service.get_agenda(agenda_id), 200

    def update_agenda(self, agenda_id: int, payload: dict) -> tuple[dict, int]:
        return self.mentoring_ops_service.update_agenda(agenda_id, payload), 200

    def delete_agenda(self, agenda_id: int) -> tuple[dict, int]:
        self.mentoring_ops_service.delete_agenda(agenda_id)
        return {"message": "Agenda removida com sucesso"}, 204

    def get_review(self, review_id: int) -> tuple[dict, int]:
        return self.mentoring_ops_service.get_review(review_id), 200

    def update_review(self, review_id: int, payload: dict) -> tuple[dict, int]:
        return self.mentoring_ops_service.update_review(review_id, payload), 200

    def delete_review(self, review_id: int) -> tuple[dict, int]:
        self.mentoring_ops_service.delete_review(review_id)
        return {"message": "Avaliação removida com sucesso"}, 204