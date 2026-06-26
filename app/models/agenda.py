from dataclasses import dataclass


@dataclass(slots=True)
class AgendaMentora:
    mentora_id: int
    data_hora: str
    usuario_id: int | None = None
    disponivel: bool = True
    agenda_id: int | None = None

    def reservar(self, usuario_id: int) -> bool:
        if not self.disponivel:
            return False
        self.usuario_id = usuario_id
        self.disponivel = False
        return True

    def liberar(self) -> bool:
        self.usuario_id = None
        self.disponivel = True
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.agenda_id,
            "mentora_id": self.mentora_id,
            "usuario_id": self.usuario_id,
            "data_hora": self.data_hora,
            "disponivel": self.disponivel,
        }