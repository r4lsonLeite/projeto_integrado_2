from dataclasses import dataclass


@dataclass(slots=True)
class Partner:
    name: str
    partner_type: str
    contact: str
    partner_id: int | None = None

    def publish_service(self, service_name: str, service_description: str) -> bool:
        return bool(service_name and service_description)

    def to_dict(self) -> dict:
        return {
            "id": self.partner_id,
            "name": self.name,
            "partner_type": self.partner_type,
            "contact": self.contact,
        }


@dataclass(slots=True)
class PartnerOffer:
    partner_id: int
    title: str
    description: str
    criteria_json: str
    enrollment_url: str
    is_active: bool = True
    offer_id: int | None = None

    def toggle_activation(self) -> bool:
        self.is_active = not self.is_active
        return self.is_active

    def to_dict(self) -> dict:
        return {
            "id": self.offer_id,
            "partner_id": self.partner_id,
            "title": self.title,
            "description": self.description,
            "criteria_json": self.criteria_json,
            "enrollment_url": self.enrollment_url,
            "is_active": self.is_active,
        }