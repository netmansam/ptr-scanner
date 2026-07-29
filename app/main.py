from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.health import database_health

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
def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "title": "PTR Scanner Dashboard"
        }
    )

