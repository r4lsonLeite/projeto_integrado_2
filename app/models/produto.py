from dataclasses import dataclass


@dataclass(slots=True)
class Produto:
    usuario_id: int
    titulo: str
    descricao: str
    valor: float
    categoria: str
    status: str = "ativo"
    produto_id: int | None = None

    def aplicar_desconto(self, percentual: float) -> bool:
        if percentual < 0 or percentual > 100:
            return False
        self.valor = round(self.valor * (1 - percentual / 100), 2)
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.produto_id,
            "usuario_id": self.usuario_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "valor": self.valor,
            "categoria": self.categoria,
            "status": self.status,
        }