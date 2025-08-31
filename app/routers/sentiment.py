from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut
from transformers import pipeline
from functools import lru_cache

router = APIRouter(prefix="/sentiment", tags=["nlp"])
MODEL_NAME = "sshleifer/tiny-distilbert-base-uncased-finetuned-sst-2-english"

@lru_cache(maxsize=1)
def get_nlp():
    # loaded on first call, then cached
    return pipeline("sentiment-analysis", model=MODEL_NAME)

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    nlp = get_nlp()
    res = nlp(payload.text)[0]
    label = res["label"].lower()
    score = float(res["score"])
    if 0.45 <= score <= 0.55:
        label = "neutral"
    return {"label": label, "score": score}
