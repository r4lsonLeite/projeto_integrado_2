from typing import Optional, Dict, Any


class Anuncio:
    def __init__(self, anuncio_id: int, produto_id: int, status_anuncio: str = 'rascunho',
                 data_publicacao: Optional[str] = None) -> None:
        self.anuncio_id = anuncio_id
        self.produto_id = produto_id
        self.status_anuncio = status_anuncio
        self.data_publicacao = data_publicacao

    def publicar(self, data_publicacao: str) -> bool:
        self.status_anuncio = 'publicado'
        self.data_publicacao = data_publicacao
        return True

    def pausar(self) -> bool:
        if self.status_anuncio == 'publicado':
            self.status_anuncio = 'pausado'
            return True
        return False

    def to_dict(self) -> Dict[str, Any]:
        return {
            'anuncio_id': self.anuncio_id,
            'produto_id': self.produto_id,
            'status_anuncio': self.status_anuncio,
            'data_publicacao': self.data_publicacao
        }
