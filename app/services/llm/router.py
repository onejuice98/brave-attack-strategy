from app.models.unit_context import UnitContext
from app.config.constants import ActionType


def route(unit: UnitContext) -> str:
    """
    유닛 상황을 기반으로 LLM 프롬프트 타입을 결정합니다.
    현재는 간단히 체력 기준으로 결정하며,
    향후 전략적으로 확장 가능.
    """
    if unit.hp < 30:
        return ActionType.DEFEND
    elif unit.enemy_in_range:
        return ActionType.ATTACK
    else:
        return ActionType.MOVE
