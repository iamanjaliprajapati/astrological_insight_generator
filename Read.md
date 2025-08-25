***
```markdown
# Astrological Insight Generator with LLM Integration

## Overview

This project provides a modular Astrological Insight Generator API that:

- Infers zodiac signs from user birth dates
- Uses simplified daily base predictions per zodiac sign
- Generates personalized, natural-language astrological insights using a Large Language Model (Hugging Face GPT-2)
- Supports basic multilingual translation (e.g., English and Hindi)
- Implements simple caching per user and day to ensure consistent daily insights

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Internet connection to download model weights on first run

### Installation

1. Clone or download the project files.

2. Create and activate a Python virtual environment (recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

### Running the API

Launch the FastAPI application:

```
python main.py
```

This will start the server at `http://127.0.0.1:8000`.

### Usage

Send a POST request to `/predict` with a JSON body containing birth and user details. Example:

```
{
  "name": "Ritika",
  "birth_date": "1995-08-20",
  "birth_time": "14:30",
  "birth_place": "Jaipur, India",
  "language": "en"
}
```

Example `curl` command:

```
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-d '{"name": "Ritika", "birth_date": "1995-08-20", "birth_time": "14:30", "birth_place": "Jaipur, India", "language": "en"}'
```

Expected response example:

```
{
  "zodiac": "Leo",
  "insight": "Your innate leadership and warmth will shine today. Embrace spontaneity and avoid overthinking.",
  "language": "en"
}
```

## Project Structure

- `main.py` — API server and routing logic
- `zodiac.py` — Logic to infer zodiac sign from birth date
- `prediction.py` — Static daily predictions for each zodiac sign
- `llm_model.py` — Wrapper to generate personalized insights using GPT-2 model
- `llm_stub.py` — Interface abstraction calling `llm_model.py`
- `translation.py` — Simple multilingual translation (English and Hindi)
- `cache.py` — In-memory caching and user scoring utilities

## Design Choices and Assumptions

### Models Used

- **Zodiac inference** is a date-range lookup, implemented in `zodiac.py`.
- **Daily predictions** are predefined strings for each zodiac (simplified static messages).
- **Personalized insight generation** leverages a GPT-2 causal language model via Hugging Face's `transformers` pipeline, chosen for its accessibility and text generation capabilities.
- **Translation** uses Facebook's NLLB-200 multilingual model, to demonstrate multilingual support, currently limited to Hindi.

### Data Flow

1. User sends birth details and language preference to `/predict`.
2. The system validates input formats for birth date/time.
3. Computes a cache key based on user info and current date for daily caching.
4. Retrieves cached response if available, else proceeds.
5. Infers the zodiac sign from the birth date.
6. Retrieves the basic daily prediction message for that zodiac.
7. Calls GPT-2 to generate a warm, uplifting, personalized astrological insight expanding on the base prediction.
8. Translates the insight if a non-English language is requested.
9. Caches the generated response for subsequent requests on the same day.
10. Returns JSON with zodiac, personalized insight, and language code.

### Assumptions

- The user's **birth date and time** are provided in standard ISO formats (`YYYY-MM-DD` and `HH:MM`).
- The daily prediction per zodiac is static and simplified, intended as a placeholder or base for personalization.
- The GPT-2 model generates relatively short, motivational messages but does not reflect full astrological complexity or real-time cosmic data.
- Translation is currently a stub for Hindi only; other languages return English text as-is.
- Caching is purely in-memory without persistence beyond the running session.
- This system is designed as a demonstration with modular extensibility for integration with advanced Panchang APIs or upgraded language models.

## Extensibility

- Integrate real Panchang APIs or Hindu astronomical data for precise predictions.
- Replace static daily messages with dynamically computed predictions.
- Upgrade the LLM to larger, more domain-specialized models or use LangChain-style prompt chaining.
- Enhance translation to support more languages and return culturally meaningful outputs.

