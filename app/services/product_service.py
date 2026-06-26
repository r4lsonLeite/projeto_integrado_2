from app.models.produto import Produto
from app.repositories.sqlite import ProductRepository, UserRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository, user_repository: UserRepository) -> None:
        self.product_repository = product_repository
        self.user_repository = user_repository

    def list_products(self) -> list[dict]:
        return [product.to_dict() for product in self.product_repository.list_all()]

    def create_product(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["usuario_id"])
        if not user:
            raise LookupError("Usuária do produto não encontrada.")

        product = Produto(
            usuario_id=payload["usuario_id"],
            titulo=payload["titulo"],
            descricao=payload["descricao"],
            valor=float(payload["valor"]),
            categoria=payload["categoria"],
            status=payload.get("status", "ativo"),
        )
        created_product = self.product_repository.create(product)
        return created_product.to_dict()