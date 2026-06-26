from dataclasses import dataclass


@dataclass(slots=True)
class AvaliacaoMentoria:
    mentoria_id: int
    nota: float
    comentario: str
    data_avaliacao: str | None = None
    avaliacao_id: int | None = None

    def atualizar_nota(self, nova_nota: float, novo_comentario: str | None = None) -> bool:
        self.nota = float(nova_nota)
        if novo_comentario is not None:
            self.comentario = novo_comentario
        return True

    def resumo(self) -> str:
        return f"Mentoria {self.mentoria_id} avaliada com nota {self.nota}: {self.comentario}"

    def to_dict(self) -> dict:
        return {
            "id": self.avaliacao_id,
            "mentoria_id": self.mentoria_id,
            "nota": self.nota,
            "comentario": self.comentario,
            "data_avaliacao": self.data_avaliacao,
        }