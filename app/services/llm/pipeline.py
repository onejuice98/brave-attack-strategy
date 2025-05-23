from app.models.unit_context import UnitContext
from app.models.response import CommanderResponse
from app.services.llm import builder, generator
from app.services.llm.retriever import VectorRetriever


def run_pipeline(unit_context: UnitContext) -> CommanderResponse:
    prompt = builder.build_prompt(unit_context)

    retriever = VectorRetriever()
    related_docs = retriever.get_context(unit_context)

    llm_generator = generator.LLMGenerator()
    response = llm_generator.run(prompt, related_docs, unit_context.commander_side)
    return response
