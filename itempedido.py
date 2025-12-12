from typing import Dict, Any


class ItemPedido:
    def __init__(self, item_id: int, pedido_id: int, produto_id: int, quantidade: int, preco_unitario: float) -> None:
        self.item_id = item_id
        self.pedido_id = pedido_id
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = float(preco_unitario)

    def calcular_total(self) -> float:
        return self.quantidade * self.preco_unitario

    def to_dict(self) -> Dict[str, Any]:
        return {
            'item_id': self.item_id,
            'pedido_id': self.pedido_id,
            'produto_id': self.produto_id,
            'quantidade': self.quantidade,
            'preco_unitario': self.preco_unitario,
            'total': self.calcular_total()
        }
