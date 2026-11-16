"""Configuration centrale de TenderAI (variables d'environnement)."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application
    app_name: str = "TenderAI API"
    environment: str = "development"
    secret_key: str = "change-me-in-production"
    access_token_expire_minutes: int = 60 * 24  # 24h

    # Base de données (Neon en prod)
    database_url: str = "postgresql+psycopg://user:password@localhost:5432/tenderai"

    # Mistral AI
    mistral_api_key: str = ""
    mistral_model: str = "mistral-large-latest"

    # CORS : origines autorisées (frontend)
    cors_origins: str = "http://localhost:3000,https://tenderai.vercel.app"

    # Stripe (mission 5)
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
