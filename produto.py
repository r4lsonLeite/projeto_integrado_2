from typing import Dict, Any


class Produto:
    def __init__(self, produto_id: int, usuario_id: int, titulo: str, descricao: str,
                 valor: float, categoria: str, status: str = 'rascunho') -> None:
        self.produto_id = produto_id
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        self.valor = float(valor)
        self.categoria = categoria
        self.status = status

    def aplicar_desconto(self, percentual: float) -> bool:
        if percentual < 0 or percentual > 100:
            return False
        self.valor = self.valor * (1 - percentual / 100)
        return True

    def atualizar_status(self, novo_status: str) -> bool:
        self.status = novo_status
        return True

    def to_dict(self) -> Dict[str, Any]:
        return {
            'produto_id': self.produto_id,
            'usuario_id': self.usuario_id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'valor': self.valor,
            'categoria': self.categoria,
            'status': self.status
        }
