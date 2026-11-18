"""Point d'entrée de l'API TenderAI."""
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

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
