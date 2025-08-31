# app/routers/sentiment.py
from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut
from transformers import pipeline

router = APIRouter(prefix="/sentiment", tags=["nlp"])

# 3-class sentiment model: labels are "negative", "neutral", "positive"
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"

# Load once at startup (cached by the process). First call may be slower due to model download.
_nlp = pipeline(task="sentiment-analysis", model=MODEL_NAME)

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    """
    Classify sentiment with a 3-class model.
    Returns the top class label (positive|neutral|negative) and its confidence score.
    """
    res = _nlp(payload.text)[0]  # e.g. {"label": "neutral", "score": 0.77}
    label = res["label"].lower()
    score = float(res["score"])
    return {"label": label, "score": score}
