from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut
from transformers import pipeline

router = APIRouter(prefix="/sentiment", tags=["nlp"])

# load once at startup
_nlp = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    res = _nlp(payload.text)[0]  # {'label': 'POSITIVE', 'score': 0.997...}
    label = res["label"].lower()
    score = float(res["score"])
    return {"label": label, "score": score}
