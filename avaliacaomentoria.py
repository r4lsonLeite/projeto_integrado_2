from typing import Optional, Dict, Any


class AvaliacaoMentoria:
    def __init__(self, avaliacao_id: int, mentoria_id: int, nota: float, comentario: str,
                 data_avaliacao: Optional[str] = None) -> None:
        self.avaliacao_id = avaliacao_id
        self.mentoria_id = mentoria_id
        self.nota = float(nota)
        self.comentario = comentario
        self.data_avaliacao = data_avaliacao

    def atualizar_nota(self, nova_nota: float, novo_comentario: Optional[str] = None) -> bool:
        self.nota = float(nova_nota)
        if novo_comentario is not None:
            self.comentario = novo_comentario
        return True

    def resumo(self) -> str:
        return f"Mentoria {self.mentoria_id} avaliada com nota {self.nota}: {self.comentario}"

    def to_dict(self) -> Dict[str, Any]:
        return {
            'avaliacao_id': self.avaliacao_id,
            'mentoria_id': self.mentoria_id,
            'nota': self.nota,
            'comentario': self.comentario,
            'data_avaliacao': self.data_avaliacao
        }
