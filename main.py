from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

from zodiac import infer_zodiac_sign
from prediction import get_daily_prediction
from llm_stub import generate_personalized_insight
from translation import translate
from cache import get_cache_key, get_cached_response, set_cached_response

app = FastAPI()

class BirthData(BaseModel):
    name: str
    birth_date: str
    birth_time: str
    birth_place: str
    language: str = "en"

@app.post("/predict")
def predict(data: BirthData):
    try:
        datetime.strptime(data.birth_date, "%Y-%m-%d")
        datetime.strptime(data.birth_time, "%H:%M")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date or time format")

    today_str = datetime.now().strftime("%Y-%m-%d")
    cache_key = get_cache_key(data.name, data.birth_date, today_str)

    cached = get_cached_response(cache_key)
    if cached:
        return cached

    zodiac = infer_zodiac_sign(data.birth_date)
    base_pred = get_daily_prediction(zodiac)

    # Updated call to pass zodiac explicitly
    personalized = generate_personalized_insight(base_pred, data.name, zodiac)
    translated = translate(personalized, data.language)


    response = {"zodiac": zodiac, "insight": translated, "language": data.language}
    set_cached_response(cache_key, response)
    return response


# Add entry point to run with python main.py
import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
