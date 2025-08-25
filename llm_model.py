from transformers import pipeline

# Load GPT-2 model for text generation (causal LM)
generator = pipeline("text-generation", model="gpt2")

def generate_personalized_insight_llm(zodiac: str, base_prediction: str, user_name: str) -> str:
    prompt = (
        f"Write a warm and uplifting daily astrological insight for {user_name}, "
        f"a {zodiac}. Base prediction: {base_prediction}."
    )
    
    output = generator(prompt, max_length=100, do_sample=True, temperature=0.8, top_p=0.9)
    generated_text = output[0]['generated_text']

    # Remove prompt echo if present
    if generated_text.startswith(prompt):
        generated_text = generated_text[len(prompt):].strip()

    if not generated_text:
        generated_text = base_prediction

    return generated_text

# from transformers import pipeline

# # Load causal language model GPT-2 for text generation
# generator = pipeline("text-generation", model="deepseek-ai/DeepSeek-V3.1-Base", trust_remote_code=True)

# def generate_personalized_insight_llm(zodiac: str, base_prediction: str, user_name: str) -> str:
#     prompt = (
#         f"""
#         You are an experienced astrologer known for giving concise, uplifting, and insightful horoscopes.  
#         Your goal is to generate a personalized horoscope that feels motivating and encouraging.  

#         ### User Information
#         - Name: {user_name}  
#         - Zodiac Sign: {zodiac}  
#         - Base Prediction: {base_prediction}  

#         ### Instructions
#         1. Write the horoscope in 2–3 sentences.  
#         2. Use a warm, positive, and motivational tone.  
#         3. Naturally expand on the base prediction without copying it word-for-word.  
#         4. Keep the message simple, clear, and uplifting — avoid jargon or negativity.  
#         5. Optionally include a subtle piece of advice related to personal growth, work, or relationships.  
#         6. Do not mention "base prediction" in the output — just integrate it smoothly.
#         7. Do not list or mention personal details like "Birthplace" or other metadata.
#         8. Provide only the horoscope message, without any headers or labels.  
#         Instructions:

#         ### Output Format
#         - Direct horoscope message only.  
#         - No headers, labels, or explanations.  

#         ### Example Style
#         ✨ "Today brings fresh opportunities for growth, {user_name}. Your {zodiac} spirit will help you stay calm and grounded, turning small challenges into moments of strength."  
#         """

#     )
#     output = generator(prompt, max_length=100, do_sample=True, temperature=0.8, top_p=0.9)
#     generated_text = output[0]['generated_text']

#     # Remove exact prompt repetition from generated text if present
#     # if generated_text.startswith(prompt):
#     #     generated_text = generated_text[len(prompt):].strip()

#     # Fallback if generation failed or output is empty
#     if not generated_text:
#         generated_text = base_prediction

#     return generated_text
