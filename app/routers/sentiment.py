# app/routers/sentiment.py
import os
from functools import lru_cache
from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut
from transformers import pipeline

router = APIRouter(prefix="/sentiment", tags=["nlp"])

# Default to the stable, small SST-2 model for reliability (works in CI)
DEFAULT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"

@lru_cache(maxsize=1)
def get_nlp():
    """Load the sentiment pipeline once, selecting model by env var.
    If the requested model fails, fall back to DEFAULT_MODEL.
    """
    model_name = os.getenv("SENTIMENT_MODEL_NAME", DEFAULT_MODEL)
    try:
        return pipeline("sentiment-analysis", model=model_name)
    except Exception:
        # Fall back to a known-good model if a tiny/corrupted model was requested
        return pipeline("sentiment-analysis", model=DEFAULT_MODEL)

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    nlp = get_nlp()
    res = nlp(payload.text)[0]  # e.g. {'label': 'POSITIVE', 'score': 0.97}
    label = res["label"].lower()  # 'positive' or 'negative'
    score = float(res["score"])

    # Add neutral band around 0.5 so API is 3-class
    if 0.45 <= score <= 0.55:
        label = "neutral"

    return {"label": label, "score": score}
