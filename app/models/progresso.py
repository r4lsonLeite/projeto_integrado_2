from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ProgressoConteudo:
    user_id: int
    conteudo_id: int
    status: str = "nao_iniciado"
    percentual: int = 0
    ultimo_acesso: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    progresso_id: int | None = None

    def marcar_progresso(self, percentual: int) -> bool:
        if percentual < 0 or percentual > 100:
            return False
        self.percentual = percentual
        self.status = "concluido" if percentual == 100 else "em_andamento"
        self.ultimo_acesso = datetime.utcnow().isoformat()
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.progresso_id,
            "user_id": self.user_id,
            "conteudo_id": self.conteudo_id,
            "status": self.status,
            "percentual": self.percentual,
            "ultimo_acesso": self.ultimo_acesso,
        }