from typing import List, Optional, Union
from enum import Enum
from app.models.response import CommanderResponse, UnitAction
from app.config.settings import settings
from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage
from langchain_core.tools import tool
from pydantic import BaseModel, Field
import json
import os


class ActionType(str, Enum):
    move = "move"
    attack = "attack"
    defend = "defend"
    skill = "skill"
    wait = "wait"


class UnitActionSchema(BaseModel):
    unit_id: str
    action: ActionType
    target: Optional[Union[str, List[float]]]
    skill_id: Optional[str]
    turn: int


class CommanderResponseSchema(BaseModel):
    commander_id: str
    unit_actions: List[List[UnitActionSchema]]


@tool(args_schema=CommanderResponseSchema)
def CommanderResponseFormatter(
    commander_id: str, unit_actions: List[List[UnitActionSchema]]
) -> dict:
    """Return the commander_id which is you provided and unit_actions in proper structured JSON format."""
    return {"commander_id": commander_id, "unit_actions": unit_actions}


class LLMGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=settings.llm_model,
            temperature=settings.temperature,
            api_key=settings.openai_api_key,
        )

        # tool binding = 무조건 JSON 출력 강제
        self.model = self.llm.bind_tools([CommanderResponseFormatter])

        # 프롬프트 템플릿 외부 파일에서 로드
        prompt_path = os.path.join("prompts", "commander.txt")
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_template_str = f.read()

            self.prompt_template = PromptTemplate(
                template=prompt_template_str,
                input_variables=["commander_side", "context", "prompt"],  # ✅ 추가됨
            )

        self.chain = self.prompt_template | self.model

    def run(
        self, prompt: str, context: List[str], commander_side: str
    ) -> CommanderResponse:
        try:
            result = self.chain.invoke(
                {
                    "commander_side": commander_side,  # ✅ 추가됨
                    "prompt": prompt,
                    "context": "\n".join(context),
                }
            )
            print("PROMT", {"prompt": prompt, "context": "\n".join(context)})
            if isinstance(result, AIMessage) and result.tool_calls:
                tool_call = result.tool_calls[0]
                args = tool_call["args"]
                raw_actions = args["unit_actions"]

                # 1차원이면 자동 변환
                if raw_actions and isinstance(raw_actions[0], dict):
                    raw_actions = [[action] for action in raw_actions]

                unit_actions = [
                    [UnitAction(**action) for action in unit_plan]
                    for unit_plan in raw_actions
                ]
                return CommanderResponse(
                    commander_id=args["commander_id"], unit_actions=unit_actions
                )

            raise ValueError("Unsupported LLM result format")

        except Exception as e:
            print("[LLM ERROR]", e)
            return CommanderResponse(commander_id="commander_error", unit_actions=[])
