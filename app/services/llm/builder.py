from app.models.unit_context import UnitContext


def build_prompt(action_type: str, unit: UnitContext) -> str:
    """
    주어진 행동 타입과 유닛 상황을 바탕으로 프롬프트 문자열을 생성합니다.
    prompts/{action_type}.txt 파일을 로드하여 상황을 삽입합니다.
    """
    try:
        with open(f"prompts/{action_type}.txt", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        template = "Given the situdation: {situation}, decide the best action."

    situation = (
        f"Unit ID: {unit.unit_id}\n"
        f"HP: {unit.hp}\n"
        f"Position: {unit.position}\n"
        f"Enemies Nearby: {unit.enemy_in_range}\n"
        f"User Command: {unit.player_command or 'None'}"
    )

    return template.format(situation=situation)
