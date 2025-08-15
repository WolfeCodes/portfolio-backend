from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

@router.get("/")
def get_projects():
    file = Path("data/projects.json")
    data = json.loads(file.read_text())
    return data
