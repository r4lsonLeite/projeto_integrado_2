from app.services.product_service import ProductService


class ProductController:
    def __init__(self, product_service: ProductService) -> None:
        self.product_service = product_service

    def list_products(self) -> tuple[list[dict], int]:
        return self.product_service.list_products(), 200

    def create_product(self, payload: dict) -> tuple[dict, int]:
        return self.product_service.create_product(payload), 201