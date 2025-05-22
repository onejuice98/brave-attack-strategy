from typing import List, Optional, Union
from app.models.response import LLMResponse
from app.config.settings import settings

from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage
from pydantic import BaseModel, Field
import json


class ResponseFormatter(BaseModel):
    """Structured output for unit action decision."""

    action: str = Field(
        description="The decided action for the unit: 'move', 'attack', 'defend', or 'wait'"
    )
    target: Optional[Union[str, List[int]]] = Field(
        default=None,
        description="The action target: enemy id, or (x, y) position, or null",
    )


class LLMGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name=settings.llm_model,
            temperature=settings.temperature,
            api_key=settings.openai_api_key,
        )

        self.model = self.llm.bind_tools([ResponseFormatter])

        self.prompt_template = PromptTemplate(
            template="""
You are a strategy game AI agent.
Based on the given context and situation, return the next action for the unit.

Context:
{context}

Situation:
{prompt}
""",
            input_variables=["context", "prompt"],
        )

        self.chain = self.prompt_template | self.model

    def run(self, prompt: str, context: List[str]) -> LLMResponse:
        try:
            result = self.chain.invoke(
                {"prompt": prompt, "context": "\n".join(context)}
            )

            if isinstance(result, AIMessage) and result.tool_calls:
                tool_call = result.tool_calls[0]
                args = tool_call["args"]
                return LLMResponse(**args)

            raise ValueError("Unsupported LLM result format")

        except Exception as e:
            print("[LLM ERROR]", e)
            return LLMResponse(action="wait", target=None)
