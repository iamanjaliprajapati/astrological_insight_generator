# Basic daily messages for each zodiac sign.
DAILY_PREDICTIONS = {
    "Aries": "Your energy will be high today. Take initiative but avoid impulsiveness.",
    "Taurus": "Ground yourself in patience today. A steady approach wins the race.",
    "Gemini": "Your curiosity brings new opportunities. Stay flexible in communication.",
    "Cancer": "Nurture your relationships. Emotional intelligence guides your decisions.",
    "Leo": "Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking.",
    "Virgo": "Attention to detail is your key strength now. Organize your thoughts clearly.",
    "Libra": "Seek balance in work and play. Harmony fosters great connections.",
    "Scorpio": "Your intensity fuels your passion. Focus it wisely to avoid burnout.",
    "Sagittarius": "Adventure calls. Keep your optimism high but watch for practical details.",
    "Capricorn": "Your discipline will open doors. Stay focused on long-term goals.",
    "Aquarius": "Innovative ideas flow easily. Collaborate to maximize impact.",
    "Pisces": "Creativity peaks. Let your intuition guide your choices today.",
}

def get_daily_prediction(zodiac: str) -> str:
    """
    Return a daily prediction string for the provided zodiac sign.
    If zodiac is unknown, return a generic message.
    """
    return DAILY_PREDICTIONS.get(zodiac, "Today is a day full of potential and growth.")
