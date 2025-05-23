from typing import List, Optional, Literal
from pydantic import BaseModel, Field


class Position(BaseModel):
    x: float
    y: float


class Skill(BaseModel):
    skill_id: str
    name: str
    cooldown: int
    is_available: bool


class UnitState(BaseModel):
    unit_id: str
    team: str = Field(description="ally or enemy")
    position: Position
    hp: int
    max_hp: int
    status: Optional[str] = Field(default=None, description="e.g., stunned, poisoned")
    action_points: int
    skills: List[Skill]
    role: Optional[str] = Field(
        default=None,
        description="Role of the unit: 'tank', 'dealer', 'supporter', 'healer'",
    )


class BattlefieldContext(BaseModel):
    turn_number: int
    terrain: Optional[str] = Field(
        default=None, description="description of terrain or map features"
    )
    objectives: Optional[str] = Field(
        default=None, description="mission goals or win conditions"
    )


class UnitContext(BaseModel):
    commander_id: str
    commander_side: Literal["ally", "enemy"]
    units: List[UnitState]
    battlefield: BattlefieldContext
