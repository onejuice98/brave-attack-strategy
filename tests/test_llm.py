from app.models.unit_context import UnitContext
from app.services.llm.pipeline import run_pipeline


def test_llm_basic():
    # 테스트 유닛 상황 생성
    unit = UnitContext(
        unit_id="U001",
        hp=100,
        position=(2, 3),
        enemy_in_range=True,
        player_command=None,
    )

    result = run_pipeline(unit)
    print("💬 LLM 응답:", result)


if __name__ == "__main__":
    test_llm_basic()
