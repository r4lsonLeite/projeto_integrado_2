from app.services.announcement_service import AnnouncementService


class AnnouncementController:
    def __init__(self, announcement_service: AnnouncementService) -> None:
        self.announcement_service = announcement_service

    def list_announcements(self) -> tuple[list[dict], int]:
        return self.announcement_service.list_announcements(), 200

    def create_announcement(self, payload: dict) -> tuple[dict, int]:
        return self.announcement_service.create_announcement(payload), 201

    def get_announcement(self, anuncio_id: int) -> tuple[dict, int]:
        return self.announcement_service.get_announcement(anuncio_id), 200

    def update_announcement(self, anuncio_id: int, payload: dict) -> tuple[dict, int]:
        return self.announcement_service.update_announcement(anuncio_id, payload), 200

    def delete_announcement(self, anuncio_id: int) -> tuple[dict, int]:
        self.announcement_service.delete_announcement(anuncio_id)
        return {"message": "Anúncio removido com sucesso"}, 204