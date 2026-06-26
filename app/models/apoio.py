from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Address:
    user_id: int
    street: str
    city: str
    country: str
    zip_code: str
    address_id: int | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.address_id,
            "user_id": self.user_id,
            "street": self.street,
            "city": self.city,
            "country": self.country,
            "zip_code": self.zip_code,
        }


@dataclass(slots=True)
class EventMetric:
    user_id: int
    event_type: str
    reference_id: str
    event_date: str
    event_id: int | None = None

    def record_event(self) -> bool:
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.event_id,
            "user_id": self.user_id,
            "event_type": self.event_type,
            "reference_id": self.reference_id,
            "event_date": self.event_date,
        }


@dataclass(slots=True)
class Notification:
    user_id: int
    channel: str
    content: str
    send_status: str = "pending"
    send_date: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    notification_id: int | None = None

    def send_notification(self) -> bool:
        if self.send_status != "pending":
            return False
        self.send_status = "sent"
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.notification_id,
            "user_id": self.user_id,
            "channel": self.channel,
            "content": self.content,
            "send_status": self.send_status,
            "send_date": self.send_date,
        }