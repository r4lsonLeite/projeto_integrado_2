from app.services.learning_ops_service import LearningOpsService


class LearningOpsController:
    def __init__(self, learning_ops_service: LearningOpsService) -> None:
        self.learning_ops_service = learning_ops_service

    def list_progress(self) -> tuple[list[dict], int]:
        return self.learning_ops_service.list_progress(), 200

    def create_progress(self, payload: dict) -> tuple[dict, int]:
        return self.learning_ops_service.create_progress(payload), 201

    def list_diagnoses(self) -> tuple[list[dict], int]:
        return self.learning_ops_service.list_diagnoses(), 200

    def create_diagnosis(self, payload: dict) -> tuple[dict, int]:
        return self.learning_ops_service.create_diagnosis(payload), 201

    def get_progress(self, progress_id: int) -> tuple[dict, int]:
        return self.learning_ops_service.get_progress(progress_id), 200

    def update_progress(self, progress_id: int, payload: dict) -> tuple[dict, int]:
        return self.learning_ops_service.update_progress(progress_id, payload), 200

    def delete_progress(self, progress_id: int) -> tuple[dict, int]:
        self.learning_ops_service.delete_progress(progress_id)
        return {"message": "Progresso removido com sucesso"}, 204

    def get_diagnosis(self, diagnosis_id: int) -> tuple[dict, int]:
        return self.learning_ops_service.get_diagnosis(diagnosis_id), 200

    def update_diagnosis(self, diagnosis_id: int, payload: dict) -> tuple[dict, int]:
        return self.learning_ops_service.update_diagnosis(diagnosis_id, payload), 200

    def delete_diagnosis(self, diagnosis_id: int) -> tuple[dict, int]:
        self.learning_ops_service.delete_diagnosis(diagnosis_id)
        return {"message": "Diagnóstico removido com sucesso"}, 204