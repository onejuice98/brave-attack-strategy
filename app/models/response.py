from typing import List, Optional, Union
from pydantic import BaseModel, Field


class UnitAction(BaseModel):
    unit_id: str = Field(description="The unique identifier for the unit.")
    action: str = Field(
        description="The decided action: 'move', 'attack', 'defend', 'skill', or 'wait'"
    )
    target: Optional[Union[str, List[float]]] = Field(
        default=None,
        description="Action target: enemy id (str), position coordinates [x, y], or null",
    )
    skill_id: Optional[str] = Field(
        default=None, description="Identifier for skill if action is 'skill', else null"
    )
    turn: int = Field(description="Turn number for this action to be executed")


class CommanderResponse(BaseModel):
    commander_id: str = Field(description="Unique identifier of LLM commander")
    unit_actions: List[List[UnitAction]] = Field(
        description="List of units' sequential action plans"
    )
