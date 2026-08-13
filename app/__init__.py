from flask import Flask

from . import persistence_models
from .api import api_blueprint
from .config import Config
from .extensions import init_extensions


def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_extensions(app)
    if app.config.get("AUTO_CREATE_DB", True):
        try:
            with app.app_context():
                from .container import container
                from .extensions import db

                db.create_all()
                container.initialize_data()
        except Exception:
            app.logger.exception("Falha ao inicializar banco de dados no startup")

    app.register_blueprint(api_blueprint)

    from .routes import register_blueprints

    register_blueprints(app)
    return app