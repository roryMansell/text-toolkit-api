# app/routers/sentiment.py
from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut
from transformers import pipeline

router = APIRouter(prefix="/sentiment", tags=["nlp"])

# Smaller binary sentiment model (fits in Render free tier)
MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

# Load once at startup
_nlp = pipeline("sentiment-analysis", model=MODEL_NAME)

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    """
    Classify sentiment with DistilBERT (POSITIVE/NEGATIVE).
    Adds a 'neutral' class if the model confidence is close to 0.5.
    """
    res = _nlp(payload.text)[0]  # {'label': 'POSITIVE', 'score': 0.55}
    label = res["label"].lower()   # 'positive' or 'negative'
    score = float(res["score"])

    # Add a neutral band if model is uncertain
    if 0.45 <= score <= 0.55:
        label = "neutral"

    return {"label": label, "score": score}
