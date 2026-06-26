import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-empreenda-mais-elas-2026")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret-key-empreenda-mais-elas-2026")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATABASE_PATH = os.getenv("DATABASE_PATH", os.path.join(BASE_DIR, "empreenda_mais_elas.db"))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{DATABASE_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTO_CREATE_DB = os.getenv("AUTO_CREATE_DB", "true").lower() == "true"
