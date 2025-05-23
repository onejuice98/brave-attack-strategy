from app.models.unit_context import (
    UnitContext,
    UnitState,
    Position,
    Skill,
    BattlefieldContext,
)
from app.services.llm.pipeline import run_pipeline
import json


def test_pipeline():
    unit_context = UnitContext(
        commander_id="commander_alpha",
        battlefield=BattlefieldContext(
            turn_number=5,
            terrain="Forest terrain with obstacles",
            objectives="Defeat all enemies.",
        ),
        units=[
            UnitState(
                unit_id="ally_01",
                team="ally",
                role="tank",
                position=Position(x=10.0, y=5.0),
                hp=80,
                max_hp=100,
                status=None,
                action_points=3,
                skills=[
                    Skill(
                        skill_id="sword_slash",
                        name="Sword Slash",
                        cooldown=0,
                        is_available=True,
                    ),
                    Skill(skill_id="heal", name="Heal", cooldown=2, is_available=False),
                ],
            ),
            UnitState(
                unit_id="ally_02",
                team="ally",
                role="dealer",
                position=Position(x=9.0, y=6.0),
                hp=60,
                max_hp=100,
                status="poisoned",
                action_points=2,
                skills=[
                    Skill(
                        skill_id="fireball",
                        name="Fireball",
                        cooldown=0,
                        is_available=True,
                    )
                ],
            ),
            UnitState(
                unit_id="enemy_01",
                team="enemy",
                role="dealer",
                position=Position(x=12.0, y=5.0),
                hp=100,
                max_hp=100,
                status=None,
                action_points=3,
                skills=[
                    Skill(
                        skill_id="poison_claw",
                        name="Poison Claw",
                        cooldown=0,
                        is_available=True,
                    )
                ],
            ),
        ],
    )

    response = run_pipeline(unit_context)
    print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    test_pipeline()
