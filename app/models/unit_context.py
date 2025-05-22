from pydantic import BaseModel
from typing import Optional, Tuple, Literal, List


class UnitContext(BaseModel):
    unit_id: str
    role: Literal["tank", "dealer", "healer", "support"]

    # 위치, 능력치
    position: Tuple[int, int]
    movement_speed: float
    hp: int
    mana: int
    attack_range: int
    attack_power: int
    magic_power: int
    critical_rate: float
    critical_damage: float
    final_damage_multiplier: float
    magic_resistance: int
    armor: int
    durability: int
    aggro_score: float

    # 스킬
    passive: str
    main_skill: str

    # 상황 정보
    terrain: Optional[str] = None
    enemy_in_range: bool
    player_command: Optional[str] = None

    # 전략 입력
    query: str
    doctrine_doc_path: Optional[str] = None  # 해당 유닛에게 적용할 전략 문서

    # 전투 맥락
    map_info: Optional[str] = None  # 부쉬 위치, 보스 위치, 오라존 등
    memory: Optional[List[str]] = (
        None  # 이전 행동들 예: ["used heal on A", "retreated"]
    )
