from app.services.mentoria_service import MentoriaService


class MentoriaController:
    def __init__(self, mentoria_service: MentoriaService) -> None:
        self.mentoria_service = mentoria_service

    def list_mentorias(self) -> tuple[list[dict], int]:
        return self.mentoria_service.list_mentorias(), 200

    def agendar(self, payload: dict) -> tuple[dict, int]:
        return self.mentoria_service.agendar(payload), 201