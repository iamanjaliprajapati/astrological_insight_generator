from llm_model import generate_personalized_insight_llm

def generate_personalized_insight(base_prediction: str, user_name: str, zodiac: str) -> str:
    return generate_personalized_insight_llm(zodiac, base_prediction, user_name)
