from dataclasses import dataclass, field
from datetime import datetime

from werkzeug.security import check_password_hash


@dataclass(slots=True)
class User:
    nome: str
    email: str
    senha_hash: str
    telefone: str | None = None
    endereco: str | None = None
    papel: str = "empreendedora"
    ativo: bool = True
    user_id: int | None = None
    criado_em: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.senha_hash, password)

    def to_dict(self) -> dict:
        return {
            "id": self.user_id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "papel": self.papel,
            "ativo": self.ativo,
            "criado_em": self.criado_em,
        }