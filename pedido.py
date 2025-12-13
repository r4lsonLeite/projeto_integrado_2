from typing import List, Optional, Dict, Any


class Pedido:
    def __init__(self, pedido_id: int, usuario_id: int, endereco_entrega: str,
                 status: str = 'criado', data_criacao: Optional[str] = None) -> None:
        self.pedido_id = pedido_id
        self.usuario_id = usuario_id
        self.endereco_entrega = endereco_entrega
        self.status = status
        self.data_criacao = data_criacao
        self.itens: List[Any] = []
        self.valor_total: float = 0.0

    def adicionar_item(self, item_pedido: Any) -> bool:
        if hasattr(item_pedido, 'pedido_id') and item_pedido.pedido_id not in (None, self.pedido_id):
            return False
        item_pedido.pedido_id = self.pedido_id
        self.itens.append(item_pedido)
        self.recalcular_total()
        return True

    def recalcular_total(self) -> float:
        self.valor_total = sum(getattr(item, 'preco_unitario', 0) * getattr(item, 'quantidade', 0) for item in self.itens)
        return self.valor_total

    def atualizar_status(self, novo_status: str) -> bool:
        self.status = novo_status
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            'pedido_id': self.pedido_id,
            'usuario_id': self.usuario_id,
            'endereco_entrega': self.endereco_entrega,
            'status': self.status,
            'data_criacao': self.data_criacao,
            'valor_total': self.valor_total,
            'itens': [item.to_dict() if hasattr(item, 'to_dict') else {
                'produto_id': getattr(item, 'produto_id', None),
                'quantidade': getattr(item, 'quantidade', None),
                'preco_unitario': getattr(item, 'preco_unitario', None)
            } for item in self.itens]
        }
