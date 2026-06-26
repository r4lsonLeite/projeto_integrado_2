from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


mentoring_ops_namespace = Namespace("mentorias-operacoes", description="Agendas e avaliações de mentorias")

agenda_input = mentoring_ops_namespace.model(
    "AgendaInput",
    {
        "mentora_id": fields.Integer(required=True),
        "data_hora": fields.String(required=True),
        "usuario_id": fields.Integer,
        "disponivel": fields.Boolean,
    },
)

agenda_output = mentoring_ops_namespace.model(
    "AgendaOutput",
    {
        "id": fields.Integer,
        "mentora_id": fields.Integer,
        "usuario_id": fields.Integer,
        "data_hora": fields.String,
        "disponivel": fields.Boolean,
    },
)

review_input = mentoring_ops_namespace.model(
    "ReviewInput",
    {
        "mentoria_id": fields.Integer(required=True),
        "nota": fields.Float(required=True),
        "comentario": fields.String(required=True),
        "data_avaliacao": fields.String,
    },
)

review_output = mentoring_ops_namespace.model(
    "ReviewOutput",
    {
        "id": fields.Integer,
        "mentoria_id": fields.Integer,
        "nota": fields.Float,
        "comentario": fields.String,
        "data_avaliacao": fields.String,
    },
)


@mentoring_ops_namespace.route("/agendas")
class AgendasResource(Resource):
    @jwt_required()
    @mentoring_ops_namespace.marshal_list_with(agenda_output)
    def get(self):
        data, status_code = container.mentoring_ops_controller.list_agendas()
        return data, status_code

    @jwt_required()
    @mentoring_ops_namespace.expect(agenda_input, validate=True)
    @mentoring_ops_namespace.marshal_with(agenda_output, code=201)
    def post(self):
        return container.mentoring_ops_controller.create_agenda(mentoring_ops_namespace.payload)


@mentoring_ops_namespace.route("/avaliacoes")
class ReviewsResource(Resource):
    @jwt_required()
    @mentoring_ops_namespace.marshal_list_with(review_output)
    def get(self):
        data, status_code = container.mentoring_ops_controller.list_reviews()
        return data, status_code

    @jwt_required()
    @mentoring_ops_namespace.expect(review_input, validate=True)
    @mentoring_ops_namespace.marshal_with(review_output, code=201)
    def post(self):
        try:
            return container.mentoring_ops_controller.create_review(mentoring_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

@mentoring_ops_namespace.route("/agendas/<int:agenda_id>")
class AgendaDetailResource(Resource):
    @mentoring_ops_namespace.marshal_with(agenda_output)
    def get(self, agenda_id):
        try:
            data, status_code = container.mentoring_ops_controller.get_agenda(agenda_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @mentoring_ops_namespace.expect(agenda_input, validate=True)
    @mentoring_ops_namespace.marshal_with(agenda_output, code=200)
    def put(self, agenda_id):
        try:
            return container.mentoring_ops_controller.update_agenda(agenda_id, mentoring_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, agenda_id):
        try:
            return container.mentoring_ops_controller.delete_agenda(agenda_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@mentoring_ops_namespace.route("/avaliacoes/<int:review_id>")
class ReviewDetailResource(Resource):
    @mentoring_ops_namespace.marshal_with(review_output)
    def get(self, review_id):
        try:
            data, status_code = container.mentoring_ops_controller.get_review(review_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @mentoring_ops_namespace.expect(review_input, validate=True)
    @mentoring_ops_namespace.marshal_with(review_output, code=200)
    def put(self, review_id):
        try:
            return container.mentoring_ops_controller.update_review(review_id, mentoring_ops_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, review_id):
        try:
            return container.mentoring_ops_controller.delete_review(review_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404
