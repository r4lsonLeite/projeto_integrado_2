from typing import Optional, Dict, Any


class Mentoria:
    def __init__(self, mentoria_id: int, agendamento_id: int, status: str = 'agendada',
                 data: Optional[str] = None, data_criacao: Optional[str] = None) -> None:
        self.mentoria_id = mentoria_id
        self.agendamento_id = agendamento_id
        self.status = status
        self.data = data
        self.data_criacao = data_criacao
        self.motivo_cancelamento: Optional[str] = None

    def iniciar(self) -> bool:
        if self.status == 'agendada':
            self.status = 'em_andamento'
            return True
        return False

    def concluir(self) -> bool:
        if self.status in ('em_andamento', 'agendada'):
            self.status = 'concluida'
            return True
        return False

    def cancelar(self, motivo: Optional[str] = None) -> bool:
        if self.status not in ('cancelada', 'concluida'):
            self.status = 'cancelada'
            self.motivo_cancelamento = motivo
            return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            'mentoria_id': self.mentoria_id,
            'agendamento_id': self.agendamento_id,
            'status': self.status,
            'data': self.data,
            'data_criacao': self.data_criacao,
            'motivo_cancelamento': self.motivo_cancelamento
        }
