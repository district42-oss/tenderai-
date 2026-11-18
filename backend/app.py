fastapi==0.115.6
uvicorn[standard]==0.34.0
sqlalchemy==2.0.36
psycopg[binary]==3.2.3
pydantic==2.10.4
pydantic-settings==2.7.0
python-dotenv==1.0.1
httpx==0.28.1"""Point d'entrée de l'API TenderAI."""
from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db

app = FastAPI(
    title=settings.app_name,
    debug=(settings.environment == "development"),
)


@app.get("/health")
def health(db: Session = Depends(get_db)):
    """Vérifie que l'API et la base de données répondent."""
    db.execute(text("SELECT 1"))
    return {"status": "ok", "app": settings.app_name, "environment": settings.environment}


if __name__ == "__main__":
    import uvicorn
.env
.env.*
!.env.example

__pycache__/
*.py[cod]
.venv/
venv/
.pytest_cache/
.vscode/
.idea/
.DS_Store
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
 ENVIRONMENT=development
SECRET_KEY=change-me-in-production
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/tenderai
MISTRAL_API_KEY=
MISTRAL_MODEL=mistral-large-latest
CORS_ORIGINS=http://localhost:3000
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
