from flask_restx import Namespace, Resource


health_namespace = Namespace("health", description="Verificações da API")


@health_namespace.route("")
class HealthResource(Resource):
    def get(self):
        return {"status": "ok", "message": "Empreenda Mais Elas API ativa"}