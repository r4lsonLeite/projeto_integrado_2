import os
import tempfile


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-empreenda-mais-elas-2026")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-secret-key-empreenda-mais-elas-2026")
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    IS_VERCEL = os.getenv("VERCEL") == "1" or bool(os.getenv("VERCEL_URL"))
    DEFAULT_DATABASE_PATH = os.path.join(tempfile.gettempdir(), "empreenda_mais_elas.db") if IS_VERCEL else os.path.join(BASE_DIR, "empreenda_mais_elas.db")
    DATABASE_PATH = os.getenv("DATABASE_PATH", DEFAULT_DATABASE_PATH)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{DATABASE_PATH}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTO_CREATE_DB = os.getenv("AUTO_CREATE_DB", "true").lower() == "true"
