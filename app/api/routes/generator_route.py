from fastapi import APIRouter
from app.models.unit_context import UnitContext
from app.models.response import CommanderResponse
from app.services.llm.pipeline import run_pipeline

router = APIRouter()


@router.post("/generate-actions", response_model=CommanderResponse)
def generate_actions(unit_context: UnitContext):
    return run_pipeline(unit_context)
