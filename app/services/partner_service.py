from app.models.parcerias import Partner, PartnerOffer
from app.repositories.sqlite import PartnerOfferRepository, PartnerRepository


class PartnerService:
    def __init__(self, partner_repository: PartnerRepository, offer_repository: PartnerOfferRepository) -> None:
        self.partner_repository = partner_repository
        self.offer_repository = offer_repository

    def list_partners(self) -> list[dict]:
        return [partner.to_dict() for partner in self.partner_repository.list_all()]

    def create_partner(self, payload: dict) -> dict:
        partner = Partner(name=payload["name"], partner_type=payload["partner_type"], contact=payload["contact"])
        created = self.partner_repository.create(partner)
        return created.to_dict()

    def list_offers(self) -> list[dict]:
        return [offer.to_dict() for offer in self.offer_repository.list_all()]

    def create_offer(self, payload: dict) -> dict:
        partner = self.partner_repository.get_by_id(payload["partner_id"])
        if not partner:
            raise LookupError("Parceiro não encontrado para a oferta.")
        offer = PartnerOffer(
            partner_id=payload["partner_id"],
            title=payload["title"],
            description=payload["description"],
            criteria_json=payload["criteria_json"],
            enrollment_url=payload["enrollment_url"],
            is_active=payload.get("is_active", True),
        )
        created = self.offer_repository.create(offer)
        return created.to_dict()

    def get_partner(self, partner_id: int) -> dict:
        partner = self.partner_repository.get_by_id(partner_id)
        if not partner:
            raise LookupError("Parceiro não encontrado.")
        return partner.to_dict()

    def update_partner(self, partner_id: int, payload: dict) -> dict:
        updated = self.partner_repository.update(partner_id, payload)
        if not updated:
            raise LookupError("Parceiro não encontrado.")
        return updated.to_dict()

    def delete_partner(self, partner_id: int) -> bool:
        deleted = self.partner_repository.delete(partner_id)
        if not deleted:
            raise LookupError("Parceiro não encontrado.")
        return True

    def get_offer(self, offer_id: int) -> dict:
        offer = self.offer_repository.get_by_id(offer_id)
        if not offer:
            raise LookupError("Oferta não encontrada.")
        return offer.to_dict()

    def update_offer(self, offer_id: int, payload: dict) -> dict:
        updated = self.offer_repository.update(offer_id, payload)
        if not updated:
            raise LookupError("Oferta não encontrada.")
        return updated.to_dict()

    def delete_offer(self, offer_id: int) -> bool:
        deleted = self.offer_repository.delete(offer_id)
        if not deleted:
            raise LookupError("Oferta não encontrada.")
        return True