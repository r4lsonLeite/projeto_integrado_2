from flask_jwt_extended import jwt_required
from flask_restx import Namespace, Resource, fields

from app.container import container


support_namespace = Namespace("suporte", description="Endereços, métricas e notificações")

address_input = support_namespace.model(
    "AddressInput",
    {
        "user_id": fields.Integer(required=True),
        "street": fields.String(required=True),
        "city": fields.String(required=True),
        "country": fields.String(required=True),
        "zip_code": fields.String(required=True),
    },
)

address_output = support_namespace.model(
    "AddressOutput",
    {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "street": fields.String,
        "city": fields.String,
        "country": fields.String,
        "zip_code": fields.String,
    },
)

metric_input = support_namespace.model(
    "MetricInput",
    {
        "user_id": fields.Integer(required=True),
        "event_type": fields.String(required=True),
        "reference_id": fields.String(required=True),
        "event_date": fields.String(required=True),
    },
)

metric_output = support_namespace.model(
    "MetricOutput",
    {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "event_type": fields.String,
        "reference_id": fields.String,
        "event_date": fields.String,
    },
)

notification_input = support_namespace.model(
    "NotificationInput",
    {
        "user_id": fields.Integer(required=True),
        "channel": fields.String(required=True),
        "content": fields.String(required=True),
        "send_status": fields.String,
        "send_date": fields.String,
        "enviar": fields.Boolean,
    },
)

notification_output = support_namespace.model(
    "NotificationOutput",
    {
        "id": fields.Integer,
        "user_id": fields.Integer,
        "channel": fields.String,
        "content": fields.String,
        "send_status": fields.String,
        "send_date": fields.String,
    },
)


@support_namespace.route("/enderecos")
class AddressesResource(Resource):
    @jwt_required()
    @support_namespace.marshal_list_with(address_output)
    def get(self):
        data, status_code = container.support_controller.list_addresses()
        return data, status_code

    @jwt_required()
    @support_namespace.expect(address_input, validate=True)
    @support_namespace.marshal_with(address_output, code=201)
    def post(self):
        try:
            return container.support_controller.create_address(support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@support_namespace.route("/metricas")
class MetricsResource(Resource):
    @jwt_required()
    @support_namespace.marshal_list_with(metric_output)
    def get(self):
        data, status_code = container.support_controller.list_metrics()
        return data, status_code

    @jwt_required()
    @support_namespace.expect(metric_input, validate=True)
    @support_namespace.marshal_with(metric_output, code=201)
    def post(self):
        try:
            return container.support_controller.create_metric(support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@support_namespace.route("/notificacoes")
class NotificationsResource(Resource):
    @jwt_required()
    @support_namespace.marshal_list_with(notification_output)
    def get(self):
        data, status_code = container.support_controller.list_notifications()
        return data, status_code

    @jwt_required()
    @support_namespace.expect(notification_input, validate=True)
    @support_namespace.marshal_with(notification_output, code=201)
    def post(self):
        try:
            return container.support_controller.create_notification(support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

@support_namespace.route("/enderecos/<int:address_id>")
class AddressDetailResource(Resource):
    @support_namespace.marshal_with(address_output)
    def get(self, address_id):
        try:
            data, status_code = container.support_controller.get_address(address_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @support_namespace.expect(address_input, validate=True)
    @support_namespace.marshal_with(address_output, code=200)
    def put(self, address_id):
        try:
            return container.support_controller.update_address(address_id, support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, address_id):
        try:
            return container.support_controller.delete_address(address_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@support_namespace.route("/metricas/<int:metric_id>")
class MetricDetailResource(Resource):
    @support_namespace.marshal_with(metric_output)
    def get(self, metric_id):
        try:
            data, status_code = container.support_controller.get_metric(metric_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @support_namespace.expect(metric_input, validate=True)
    @support_namespace.marshal_with(metric_output, code=200)
    def put(self, metric_id):
        try:
            return container.support_controller.update_metric(metric_id, support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, metric_id):
        try:
            return container.support_controller.delete_metric(metric_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@support_namespace.route("/notificacoes/<int:notification_id>")
class NotificationDetailResource(Resource):
    @support_namespace.marshal_with(notification_output)
    def get(self, notification_id):
        try:
            data, status_code = container.support_controller.get_notification(notification_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @support_namespace.expect(notification_input, validate=True)
    @support_namespace.marshal_with(notification_output, code=200)
    def put(self, notification_id):
        try:
            return container.support_controller.update_notification(notification_id, support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, notification_id):
        try:
            return container.support_controller.delete_notification(notification_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404


@support_namespace.route("/enderecos/<int:address_id>")
class AddressDetailResource(Resource):
    @support_namespace.marshal_with(address_output)
    def get(self, address_id):
        try:
            data, status_code = container.support_controller.get_address(address_id)
            return data, status_code
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    @support_namespace.expect(address_input, validate=True)
    @support_namespace.marshal_with(address_output, code=200)
    def put(self, address_id):
        try:
            return container.support_controller.update_address(address_id, support_namespace.payload)
        except LookupError as exc:
            return {"message": str(exc)}, 404

    @jwt_required()
    def delete(self, address_id):
        try:
            return container.support_controller.delete_address(address_id)
        except LookupError as exc:
            return {"message": str(exc)}, 404
