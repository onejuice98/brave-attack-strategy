from app.models.unit_context import UnitContext
from app.models.response import LLMResponse
from app.services.llm import router, builder, retriever, generator


def run_pipeline(unit: UnitContext) -> LLMResponse:
    action_type = router.route(unit)
    prompt = builder.build_prompt(action_type, unit)
    related_docs = retriever.get_context(unit)
    LLMGenerator = generator.LLMGenerator()
    response = LLMGenerator.run(prompt, related_docs)
    return response
