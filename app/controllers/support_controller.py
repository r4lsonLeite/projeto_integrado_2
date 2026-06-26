from app.services.support_service import SupportService


class SupportController:
    def __init__(self, support_service: SupportService) -> None:
        self.support_service = support_service

    def list_addresses(self) -> tuple[list[dict], int]:
        return self.support_service.list_addresses(), 200

    def create_address(self, payload: dict) -> tuple[dict, int]:
        return self.support_service.create_address(payload), 201

    def list_metrics(self) -> tuple[list[dict], int]:
        return self.support_service.list_metrics(), 200

    def create_metric(self, payload: dict) -> tuple[dict, int]:
        return self.support_service.create_metric(payload), 201

    def list_notifications(self) -> tuple[list[dict], int]:
        return self.support_service.list_notifications(), 200

    def create_notification(self, payload: dict) -> tuple[dict, int]:
        return self.support_service.create_notification(payload), 201

    def get_address(self, address_id: int) -> tuple[dict, int]:
        return self.support_service.get_address(address_id), 200

    def update_address(self, address_id: int, payload: dict) -> tuple[dict, int]:
        return self.support_service.update_address(address_id, payload), 200

    def delete_address(self, address_id: int) -> tuple[dict, int]:
        self.support_service.delete_address(address_id)
        return {"message": "Endereço removido com sucesso"}, 204

    def get_metric(self, metric_id: int) -> tuple[dict, int]:
        return self.support_service.get_metric(metric_id), 200

    def update_metric(self, metric_id: int, payload: dict) -> tuple[dict, int]:
        return self.support_service.update_metric(metric_id, payload), 200

    def delete_metric(self, metric_id: int) -> tuple[dict, int]:
        self.support_service.delete_metric(metric_id)
        return {"message": "Métrica removida com sucesso"}, 204

    def get_notification(self, notification_id: int) -> tuple[dict, int]:
        return self.support_service.get_notification(notification_id), 200

    def update_notification(self, notification_id: int, payload: dict) -> tuple[dict, int]:
        return self.support_service.update_notification(notification_id, payload), 200

    def delete_notification(self, notification_id: int) -> tuple[dict, int]:
        self.support_service.delete_notification(notification_id)
        return {"message": "Notificação removida com sucesso"}, 204