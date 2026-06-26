from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Mentoria:
    usuario_id: int
    mentora: str
    data_hora: str
    tema: str
    observacoes: str | None = None
    status: str = "agendada"
    mentoria_id: int | None = None
    criado_em: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def atualizar_status(self, novo_status: str) -> None:
        self.status = novo_status

    def to_dict(self) -> dict:
        return {
            "id": self.mentoria_id,
            "usuario_id": self.usuario_id,
            "mentora": self.mentora,
            "data_hora": self.data_hora,
            "tema": self.tema,
            "observacoes": self.observacoes,
            "status": self.status,
            "criado_em": self.criado_em,
        }