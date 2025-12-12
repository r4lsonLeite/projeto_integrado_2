from typing import Optional, Dict, Any


class AgendaMentora:
    def __init__(self, agenda_id: int, mentora_id: int, usuario_id: Optional[int] = None,
                 data_hora: Optional[str] = None, disponivel: bool = True) -> None:
        self.agenda_id = agenda_id
        self.mentora_id = mentora_id
        self.usuario_id = usuario_id
        self.data_hora = data_hora
        self.disponivel = disponivel

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

    def to_dict(self) -> Dict[str, Any]:
        return {
            'agenda_id': self.agenda_id,
            'mentora_id': self.mentora_id,
            'usuario_id': self.usuario_id,
            'data_hora': self.data_hora,
            'disponivel': self.disponivel
        }
