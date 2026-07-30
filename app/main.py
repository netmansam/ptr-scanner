from pathlib import Path

from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.services.health import database_health
from app.database.connection import get_db
from app.services.dashboard import get_latest_scan

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="PTR Scanner",
    version="1.0"
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)

@app.get("/health")
def health():
    return {
        "status": "online",
        "application": "PTR Scanner"
    }

@app.get("/database-health")
def db_health():

    return database_health()


@app.get("/", response_class=HTMLResponse)
def dashboard(
    request: Request,
    db: Session = Depends(get_db)
):

    scan = get_latest_scan(db)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "title": "PTR Scanner Dashboard",
            "scan": scan
        }
    )

