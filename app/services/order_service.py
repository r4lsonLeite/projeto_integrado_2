from app.models.pedido import ItemPedido, Pedido
from app.repositories.sqlite import OrderRepository, ProductRepository, UserRepository


class OrderService:
    def __init__(
        self,
        order_repository: OrderRepository,
        product_repository: ProductRepository,
        user_repository: UserRepository,
    ) -> None:
        self.order_repository = order_repository
        self.product_repository = product_repository
        self.user_repository = user_repository

    def list_orders(self) -> list[dict]:
        return [order.to_dict() for order in self.order_repository.list_all()]

    def create_order(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["usuario_id"])
        if not user:
            raise LookupError("Usuária do pedido não encontrada.")

        order = Pedido(usuario_id=payload["usuario_id"], endereco_entrega=payload["endereco_entrega"])
        for item_payload in payload["itens"]:
            product = self.product_repository.get_by_id(item_payload["produto_id"])
            if not product:
                raise LookupError(f"Produto {item_payload['produto_id']} não encontrado.")
            item = ItemPedido(
                produto_id=product.produto_id,
                quantidade=int(item_payload["quantidade"]),
                preco_unitario=product.valor,
            )
            order.adicionar_item(item)

        created_order = self.order_repository.create(order)
        return created_order.to_dict()