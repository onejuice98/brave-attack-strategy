from typing import List
from app.models.unit_context import UnitContext
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings
from app.config.settings import settings
import os


class VectorRetriever:
    def __init__(self):
        self.vectorstore_path = os.path.join("data", "vector_store")
        self.embedding_model = OpenAIEmbeddings(openai_api_key=settings.openai_api_key)
        self.vectorstore = FAISS.load_local(
            self.vectorstore_path,
            self.embedding_model,
            allow_dangerous_deserialization=True,
        )

    def make_query(self, unit_context: UnitContext) -> str:
        # 매우 간단한 예시: 전장 요약 + 아군 유닛 ID + 적군 수
        allies = [u.unit_id for u in unit_context.units if u.team == "ally"]
        enemies = [u.unit_id for u in unit_context.units if u.team == "enemy"]
        objective = unit_context.battlefield.objectives or "None"
        terrain = unit_context.battlefield.terrain or "unknown terrain"
        return (
            f"Strategy for turn {unit_context.battlefield.turn_number} "
            f"on {terrain}. Objective: {objective}. "
            f"Allies: {', '.join(allies)}. Enemies: {', '.join(enemies)}."
        )

    def get_context(self, unit_context: UnitContext) -> List[str]:
        query = self.make_query(unit_context)
        docs = self.vectorstore.similarity_search(query, k=4)
        return [doc.page_content for doc in docs]
