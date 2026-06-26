from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


learning_ops_namespace = Namespace("aprendizagem", description="Diagnósticos e progresso de conteúdo")

progress_input = learning_ops_namespace.model(
    "ProgressInput",
    {
        "user_id": fields.Integer(required=True),
        "conteudo_id": fields.Integer(required=True),
        "status": fields.String,
        "percentual": fields.Integer,
        "ultimo_acesso": fields.String,
    },
)

progress_output = learning_ops_namespace.model(
    "ProgressOutput",
    {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "conteudo_id": fields.Integer,
        "status": fields.String,
        "percentual": fields.Integer,
        "ultimo_acesso": fields.String,
    },
)

diagnosis_input = learning_ops_namespace.model(
    "DiagnosisInput",
    {
        "user_id": fields.Integer(required=True),
        "score_first": fields.Float(required=True),
        "level": fields.String(required=True),
        "answers": fields.Raw(required=True),
        "date_app": fields.String,
    },
)

diagnosis_output = learning_ops_namespace.model(
    "DiagnosisOutput",
    {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "score_first": fields.Float,
        "level": fields.String,
        "answers": fields.Raw,
        "date_app": fields.String,
    },
)


@learning_ops_namespace.route("/progressos")
class ProgressResource(Resource):
    @jwt_required()
    @learning_ops_namespace.marshal_list_with(progress_output)
    def get(self):
        data, status_code = container.learning_ops_controller.list_progress()
        return data, status_code

    @jwt_required()
    @learning_ops_namespace.expect(progress_input, validate=True)
    @learning_ops_namespace.marshal_with(progress_output, code=201)
    def post(self):
        try:
            return container.learning_ops_controller.create_progress(learning_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@learning_ops_namespace.route("/diagnosticos")
class DiagnosesResource(Resource):
    @jwt_required()
    @learning_ops_namespace.marshal_list_with(diagnosis_output)
    def get(self):
        data, status_code = container.learning_ops_controller.list_diagnoses()
        return data, status_code

    @jwt_required()
    @learning_ops_namespace.expect(diagnosis_input, validate=True)
    @learning_ops_namespace.marshal_with(diagnosis_output, code=201)
    def post(self):
        try:
            return container.learning_ops_controller.create_diagnosis(learning_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

@learning_ops_namespace.route("/progressos/<int:progress_id>")
class ProgressDetailResource(Resource):
    @learning_ops_namespace.marshal_with(progress_output)
    def get(self, progress_id):
        try:
            data, status_code = container.learning_ops_controller.get_progress(progress_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @learning_ops_namespace.expect(progress_input, validate=True)
    @learning_ops_namespace.marshal_with(progress_output, code=200)
    def put(self, progress_id):
        try:
            return container.learning_ops_controller.update_progress(progress_id, learning_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, progress_id):
        try:
            return container.learning_ops_controller.delete_progress(progress_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@learning_ops_namespace.route("/diagnosticos/<int:diagnosis_id>")
class DiagnosisDetailResource(Resource):
    @learning_ops_namespace.marshal_with(diagnosis_output)
    def get(self, diagnosis_id):
        try:
            data, status_code = container.learning_ops_controller.get_diagnosis(diagnosis_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @learning_ops_namespace.expect(diagnosis_input, validate=True)
    @learning_ops_namespace.marshal_with(diagnosis_output, code=200)
    def put(self, diagnosis_id):
        try:
            return container.learning_ops_controller.update_diagnosis(diagnosis_id, learning_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, diagnosis_id):
        try:
            return container.learning_ops_controller.delete_diagnosis(diagnosis_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404
