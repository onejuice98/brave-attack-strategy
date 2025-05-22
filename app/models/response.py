from pydantic import BaseModel
from typing import Optional, Union, Literal, List, Tuple


class LLMResponse(BaseModel):
    action: Literal["attack", "move", "defend", "use_skill", "wait"]
    target: Optional[Union[str, List[int], Tuple[int, int]]] = None
    skill_name: Optional[str] = None  # 사용할 스킬이 명시되는 경우
    direction: Optional[str] = None  # move 시: "up", "down", "left", "right"
    reason: Optional[str] = None  # 왜 이런 판단을 했는지 (설명)
