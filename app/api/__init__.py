from flask import Blueprint
from flask_restx import Api

from .namespaces.announcements_namespace import announcements_namespace
from .namespaces.auth_namespace import auth_namespace
from .namespaces.finance_namespace import finance_namespace
from .namespaces.health_namespace import health_namespace
from .namespaces.learning_ops_namespace import learning_ops_namespace
from .namespaces.mentorias_namespace import mentorias_namespace
from .namespaces.mentoring_ops_namespace import mentoring_ops_namespace
from .namespaces.orders_namespace import orders_namespace
from .namespaces.partners_namespace import partners_namespace
from .namespaces.products_namespace import products_namespace
from .namespaces.support_namespace import support_namespace
from .namespaces.trilhas_namespace import trilhas_namespace
from .namespaces.users_namespace import users_namespace

api_blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    api_blueprint,
    title="Empreenda Mais Elas API",
    version="1.0.0",
    description="API REST do backend Flask estruturado em MVC.",
    doc="/docs",
)

api.add_namespace(health_namespace)
api.add_namespace(auth_namespace)
api.add_namespace(users_namespace)
api.add_namespace(products_namespace)
api.add_namespace(announcements_namespace)
api.add_namespace(orders_namespace)
api.add_namespace(mentorias_namespace)
api.add_namespace(mentoring_ops_namespace)
api.add_namespace(trilhas_namespace)
api.add_namespace(partners_namespace)
api.add_namespace(finance_namespace)
api.add_namespace(support_namespace)
api.add_namespace(learning_ops_namespace)