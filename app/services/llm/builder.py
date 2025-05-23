from app.models.unit_context import UnitContext, UnitState, Skill


def build_prompt(unit_context: UnitContext) -> str:
    lines = []

    # 전장 정보 요약
    battlefield = unit_context.battlefield
    lines.append(f"Current Turn: {battlefield.turn_number}")
    if battlefield.terrain:
        lines.append(f"Terrain: {battlefield.terrain}")
    if battlefield.objectives:
        lines.append(f"Objective: {battlefield.objectives}")
    lines.append("")  # 줄바꿈

    # 유닛 정보 요약
    for unit in unit_context.units:
        line = (
            f"[{unit.team.upper()}] Unit '{unit.unit_id}' ({unit.role}) at ({unit.position.x}, {unit.position.y}) "
            f"HP: {unit.hp}/{unit.max_hp}, AP: {unit.action_points}"
        )
        if unit.status:
            line += f", Status: {unit.status}"
        lines.append(line)

        if unit.skills:
            skill_descriptions = []
            for skill in unit.skills:
                available = "✔" if skill.is_available else f"❌ (CD {skill.cooldown})"
                skill_descriptions.append(f"{skill.name}{available}")
            lines.append("   Skills: " + ", ".join(skill_descriptions))

    lines.append("")  # 줄바꿈

    # 요청 작업
    lines.append(
        "Commander's Intent: Determine the next strategic actions for each ally unit."
    )

    return "\n".join(lines)
