from app.models.apoio import Address, EventMetric, Notification
from app.repositories.sqlite import AddressRepository, EventMetricRepository, NotificationRepository, UserRepository


class SupportService:
    def __init__(
        self,
        address_repository: AddressRepository,
        metric_repository: EventMetricRepository,
        notification_repository: NotificationRepository,
        user_repository: UserRepository,
    ) -> None:
        self.address_repository = address_repository
        self.metric_repository = metric_repository
        self.notification_repository = notification_repository
        self.user_repository = user_repository

    def list_addresses(self) -> list[dict]:
        return [address.to_dict() for address in self.address_repository.list_all()]

    def create_address(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["user_id"])
        if not user:
            raise LookupError("Usuária não encontrada para endereço.")
        address = Address(user_id=payload["user_id"], street=payload["street"], city=payload["city"], country=payload["country"], zip_code=payload["zip_code"])
        created = self.address_repository.create(address)
        return created.to_dict()

    def list_metrics(self) -> list[dict]:
        return [metric.to_dict() for metric in self.metric_repository.list_all()]

    def create_metric(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["user_id"])
        if not user:
            raise LookupError("Usuária não encontrada para métrica.")
        metric = EventMetric(user_id=payload["user_id"], event_type=payload["event_type"], reference_id=payload["reference_id"], event_date=payload["event_date"])
        created = self.metric_repository.create(metric)
        return created.to_dict()

    def list_notifications(self) -> list[dict]:
        return [notification.to_dict() for notification in self.notification_repository.list_all()]

    def create_notification(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["user_id"])
        if not user:
            raise LookupError("Usuária não encontrada para notificação.")
        notification = Notification(user_id=payload["user_id"], channel=payload["channel"], content=payload["content"], send_status=payload.get("send_status", "pending"), send_date=payload.get("send_date") or user.criado_em)
        if payload.get("enviar", True):
            notification.send_notification()
        created = self.notification_repository.create(notification)
        return created.to_dict()

    def get_address(self, address_id: int) -> dict:
        address = self.address_repository.get_by_id(address_id)
        if not address:
            raise LookupError("Endereço não encontrado.")
        return address.to_dict()

    def update_address(self, address_id: int, payload: dict) -> dict:
        address = self.address_repository.get_by_id(address_id)
        if not address:
            raise LookupError("Endereço não encontrado.")
        return address.to_dict()

    def delete_address(self, address_id: int) -> bool:
        address = self.address_repository.get_by_id(address_id)
        if not address:
            raise LookupError("Endereço não encontrado.")
        return True

    def get_metric(self, metric_id: int) -> dict:
        metric = self.metric_repository.get_by_id(metric_id)
        if not metric:
            raise LookupError("Métrica não encontrada.")
        return metric.to_dict()

    def update_metric(self, metric_id: int, payload: dict) -> dict:
        metric = self.metric_repository.get_by_id(metric_id)
        if not metric:
            raise LookupError("Métrica não encontrada.")
        return metric.to_dict()

    def delete_metric(self, metric_id: int) -> bool:
        metric = self.metric_repository.get_by_id(metric_id)
        if not metric:
            raise LookupError("Métrica não encontrada.")
        return True

    def get_notification(self, notification_id: int) -> dict:
        notification = self.notification_repository.get_by_id(notification_id)
        if not notification:
            raise LookupError("Notificação não encontrada.")
        return notification.to_dict()

    def update_notification(self, notification_id: int, payload: dict) -> dict:
        notification = self.notification_repository.get_by_id(notification_id)
        if not notification:
            raise LookupError("Notificação não encontrada.")
        return notification.to_dict()

    def delete_notification(self, notification_id: int) -> bool:
        notification = self.notification_repository.get_by_id(notification_id)
        if not notification:
            raise LookupError("Notificação não encontrada.")
        return True