from dataclasses import dataclass


@dataclass(slots=True)
class Anuncio:
    produto_id: int
    status_anuncio: str = "rascunho"
    data_publicacao: str | None = None
    anuncio_id: int | None = None

    def publicar(self, data_publicacao: str) -> bool:
        self.status_anuncio = "publicado"
        self.data_publicacao = data_publicacao
        return True

    def pausar(self) -> bool:
        if self.status_anuncio != "publicado":
            return False
        self.status_anuncio = "pausado"
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.anuncio_id,
            "produto_id": self.produto_id,
            "status_anuncio": self.status_anuncio,
            "data_publicacao": self.data_publicacao,
        }