from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ItemPedido:
    produto_id: int
    quantidade: int
    preco_unitario: float

    def calcular_total(self) -> float:
        return round(self.quantidade * self.preco_unitario, 2)

    def to_dict(self) -> dict:
        return {
            "produto_id": self.produto_id,
            "quantidade": self.quantidade,
            "preco_unitario": self.preco_unitario,
            "total": self.calcular_total(),
        }


@dataclass(slots=True)
class Pedido:
    usuario_id: int
    endereco_entrega: str
    status: str = "criado"
    pedido_id: int | None = None
    data_criacao: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    itens: list[ItemPedido] = field(default_factory=list)
    valor_total: float = 0.0

    def adicionar_item(self, item: ItemPedido) -> None:
        self.itens.append(item)
        self.recalcular_total()

    def recalcular_total(self) -> float:
        self.valor_total = round(sum(item.calcular_total() for item in self.itens), 2)
        return self.valor_total

    def to_dict(self) -> dict:
        return {
            "id": self.pedido_id,
            "usuario_id": self.usuario_id,
            "endereco_entrega": self.endereco_entrega,
            "status": self.status,
            "data_criacao": self.data_criacao,
            "valor_total": self.valor_total,
            "itens": [item.to_dict() for item in self.itens],
        }