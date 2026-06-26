from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager


jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()


def init_extensions(app) -> None:
    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
