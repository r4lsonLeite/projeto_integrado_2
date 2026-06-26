from app.services.order_service import OrderService


class OrderController:
    def __init__(self, order_service: OrderService) -> None:
        self.order_service = order_service

    def list_orders(self) -> tuple[list[dict], int]:
        return self.order_service.list_orders(), 200

    def create_order(self, payload: dict) -> tuple[dict, int]:
        return self.order_service.create_order(payload), 201