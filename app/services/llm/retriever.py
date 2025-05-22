from app.models.unit_context import UnitContext
from typing import List


def get_context(unit: UnitContext) -> List[str]:
    """
    상황에 맞는 배경 지식을 벡터 검색으로 가져옵니다.
    현재는 단순히 예시 텍스트를 반환하지만,
    추후 FAISS나 Chroma 연동 시 이곳에서 문서 검색 수행.
    """
    # TODO: FAISS나 벡터 스토어 연동 시 교체
    dummy_knowledge = [
        "Units with low HP should prioritize defense or retreat.",
        "If an enemy is within range, attack actions are possible.",
        "Movement should consider terrain and enemy visibility.",
    ]

    return dummy_knowledge
