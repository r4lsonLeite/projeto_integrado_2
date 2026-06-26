from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Conteudo:
    conteudo_id: int
    titulo: str
    descricao: str
    categoria: str
    url: str
    carga_horaria: int

    def to_dict(self) -> dict:
        return {
            "id": self.conteudo_id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "categoria": self.categoria,
            "url": self.url,
            "carga_horaria": self.carga_horaria,
        }


@dataclass(slots=True)
class TrilhaItem:
    ordem: int
    obrigatorio: bool
    conteudo: Conteudo

    def to_dict(self) -> dict:
        return {
            "ordem": self.ordem,
            "obrigatorio": self.obrigatorio,
            "conteudo": self.conteudo.to_dict(),
        }


@dataclass(slots=True)
class Trilha:
    usuario_id: int
    tipo: str
    status: str = "ativa"
    trilha_id: int | None = None
    criado_em: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    itens: list[TrilhaItem] = field(default_factory=list)

    def adicionar_item(self, item: TrilhaItem) -> None:
        self.itens.append(item)

    def to_dict(self) -> dict:
        return {
            "id": self.trilha_id,
            "usuario_id": self.usuario_id,
            "tipo": self.tipo,
            "status": self.status,
            "criado_em": self.criado_em,
            "itens": [item.to_dict() for item in self.itens],
        }