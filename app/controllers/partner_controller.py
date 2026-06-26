from app.services.partner_service import PartnerService


class PartnerController:
    def __init__(self, partner_service: PartnerService) -> None:
        self.partner_service = partner_service

    def list_partners(self) -> tuple[list[dict], int]:
        return self.partner_service.list_partners(), 200

    def create_partner(self, payload: dict) -> tuple[dict, int]:
        return self.partner_service.create_partner(payload), 201

    def list_offers(self) -> tuple[list[dict], int]:
        return self.partner_service.list_offers(), 200

    def create_offer(self, payload: dict) -> tuple[dict, int]:
        return self.partner_service.create_offer(payload), 201

    def get_partner(self, partner_id: int) -> tuple[dict, int]:
        return self.partner_service.get_partner(partner_id), 200

    def update_partner(self, partner_id: int, payload: dict) -> tuple[dict, int]:
        return self.partner_service.update_partner(partner_id, payload), 200

    def delete_partner(self, partner_id: int) -> tuple[dict, int]:
        self.partner_service.delete_partner(partner_id)
        return {"message": "Parceiro removido com sucesso"}, 204

    def get_offer(self, offer_id: int) -> tuple[dict, int]:
        return self.partner_service.get_offer(offer_id), 200

    def update_offer(self, offer_id: int, payload: dict) -> tuple[dict, int]:
        return self.partner_service.update_offer(offer_id, payload), 200

    def delete_offer(self, offer_id: int) -> tuple[dict, int]:
        self.partner_service.delete_offer(offer_id)
        return {"message": "Oferta removida com sucesso"}, 204