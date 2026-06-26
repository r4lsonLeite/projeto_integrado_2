from app.models.trilha import Trilha, TrilhaItem
from app.repositories.sqlite import ConteudoRepository, TrilhaRepository, UserRepository


class TrilhaService:
    def __init__(
        self,
        trilha_repository: TrilhaRepository,
        conteudo_repository: ConteudoRepository,
        user_repository: UserRepository,
    ) -> None:
        self.trilha_repository = trilha_repository
        self.conteudo_repository = conteudo_repository
        self.user_repository = user_repository

    def list_trilhas(self) -> list[dict]:
        return [trilha.to_dict() for trilha in self.trilha_repository.list_all()]

    def create_trilha(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["usuario_id"])
        if not user:
            raise LookupError("Usuária da trilha não encontrada.")

        trilha = Trilha(usuario_id=payload["usuario_id"], tipo=payload["tipo"], status=payload.get("status", "ativa"))
        conteudos = self.conteudo_repository.list_all()
        for ordem, conteudo in enumerate(conteudos, start=1):
            trilha.adicionar_item(TrilhaItem(ordem=ordem, obrigatorio=ordem <= 2, conteudo=conteudo))

        created_trilha = self.trilha_repository.create(trilha)
        return created_trilha.to_dict()