from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Diagnostico:
    user_id: int
    score_first: float
    level: str
    answers: list[str] | dict
    date_app: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    diagnostico_id: int | None = None

    def resumo(self) -> str:
        return f"Diagnostico do usuario {self.user_id} com score {self.score_first} e nivel {self.level}"

    def to_dict(self) -> dict:
        return {
            "id": self.diagnostico_id,
            "user_id": self.user_id,
            "score_first": self.score_first,
            "level": self.level,
            "answers": self.answers,
            "date_app": self.date_app,
        }