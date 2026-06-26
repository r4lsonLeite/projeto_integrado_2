from app.models.marketplace import Anuncio
from app.repositories.sqlite import AnnouncementRepository, ProductRepository


class AnnouncementService:
    def __init__(self, announcement_repository: AnnouncementRepository, product_repository: ProductRepository) -> None:
        self.announcement_repository = announcement_repository
        self.product_repository = product_repository

    def list_announcements(self) -> list[dict]:
        return [announcement.to_dict() for announcement in self.announcement_repository.list_all()]

    def create_announcement(self, payload: dict) -> dict:
        product = self.product_repository.get_by_id(payload["produto_id"])
        if not product:
            raise LookupError("Produto do anúncio não encontrado.")
        announcement = Anuncio(produto_id=payload["produto_id"])
        if payload.get("data_publicacao"):
            announcement.publicar(payload["data_publicacao"])
        created = self.announcement_repository.create(announcement)
        return created.to_dict()

    def get_announcement(self, anuncio_id: int) -> dict:
        announcement = self.announcement_repository.get_by_id(anuncio_id)
        if not announcement:
            raise LookupError("Anúncio não encontrado.")
        return announcement.to_dict()

    def update_announcement(self, anuncio_id: int, payload: dict) -> dict:
        updated = self.announcement_repository.update(anuncio_id, payload)
        if not updated:
            raise LookupError("Anúncio não encontrado.")
        return updated.to_dict()

    def delete_announcement(self, anuncio_id: int) -> bool:
        deleted = self.announcement_repository.delete(anuncio_id)
        if not deleted:
            raise LookupError("Anúncio não encontrado.")
        return True