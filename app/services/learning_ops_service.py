from app.models.diagnostico import Diagnostico
from app.models.progresso import ProgressoConteudo
from app.repositories.sqlite import ContentProgressRepository, ConteudoRepository, DiagnosisRepository, UserRepository


class LearningOpsService:
    def __init__(
        self,
        progress_repository: ContentProgressRepository,
        diagnosis_repository: DiagnosisRepository,
        conteudo_repository: ConteudoRepository,
        user_repository: UserRepository,
    ) -> None:
        self.progress_repository = progress_repository
        self.diagnosis_repository = diagnosis_repository
        self.conteudo_repository = conteudo_repository
        self.user_repository = user_repository

    def list_progress(self) -> list[dict]:
        return [progress.to_dict() for progress in self.progress_repository.list_all()]

    def create_progress(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["user_id"])
        conteudo = self.conteudo_repository.get_by_id(payload["conteudo_id"])
        if not user:
            raise LookupError("Usuária não encontrada para progresso.")
        if not conteudo:
            raise LookupError("Conteúdo não encontrado para progresso.")
        progress = ProgressoConteudo(user_id=payload["user_id"], conteudo_id=payload["conteudo_id"], status=payload.get("status", "nao_iniciado"), percentual=int(payload.get("percentual", 0)), ultimo_acesso=payload.get("ultimo_acesso") or user.criado_em)
        created = self.progress_repository.create(progress)
        return created.to_dict()

    def list_diagnoses(self) -> list[dict]:
        return [diagnosis.to_dict() for diagnosis in self.diagnosis_repository.list_all()]

    def create_diagnosis(self, payload: dict) -> dict:
        user = self.user_repository.get_by_id(payload["user_id"])
        if not user:
            raise LookupError("Usuária não encontrada para diagnóstico.")
        diagnosis = Diagnostico(user_id=payload["user_id"], score_first=float(payload["score_first"]), level=payload["level"], answers=payload["answers"], date_app=payload.get("date_app") or user.criado_em)
        created = self.diagnosis_repository.create(diagnosis)
        return created.to_dict()

    def get_progress(self, progress_id: int) -> dict:
        progress = self.progress_repository.get_by_id(progress_id)
        if not progress:
            raise LookupError("Progresso não encontrado.")
        return progress.to_dict()

    def update_progress(self, progress_id: int, payload: dict) -> dict:
        progress = self.progress_repository.get_by_id(progress_id)
        if not progress:
            raise LookupError("Progresso não encontrado.")
        return progress.to_dict()

    def delete_progress(self, progress_id: int) -> bool:
        progress = self.progress_repository.get_by_id(progress_id)
        if not progress:
            raise LookupError("Progresso não encontrado.")
        return True

    def get_diagnosis(self, diagnosis_id: int) -> dict:
        diagnosis = self.diagnosis_repository.get_by_id(diagnosis_id)
        if not diagnosis:
            raise LookupError("Diagnóstico não encontrado.")
        return diagnosis.to_dict()

    def update_diagnosis(self, diagnosis_id: int, payload: dict) -> dict:
        diagnosis = self.diagnosis_repository.get_by_id(diagnosis_id)
        if not diagnosis:
            raise LookupError("Diagnóstico não encontrado.")
        return diagnosis.to_dict()

    def delete_diagnosis(self, diagnosis_id: int) -> bool:
        diagnosis = self.diagnosis_repository.get_by_id(diagnosis_id)
        if not diagnosis:
            raise LookupError("Diagnóstico não encontrado.")
        return True