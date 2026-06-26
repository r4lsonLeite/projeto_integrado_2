from app.services.trilha_service import TrilhaService


class TrilhaController:
    def __init__(self, trilha_service: TrilhaService) -> None:
        self.trilha_service = trilha_service

    def list_trilhas(self) -> tuple[list[dict], int]:
        return self.trilha_service.list_trilhas(), 200

    def create_trilha(self, payload: dict) -> tuple[dict, int]:
        return self.trilha_service.create_trilha(payload), 201