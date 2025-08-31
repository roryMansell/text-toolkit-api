from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut

router = APIRouter(prefix="/sentiment", tags=["nlp"])

# Very simple keyword-based sentiment system
POSITIVE = {"love", "great", "happy", "good", "fantastic", "excellent", "awesome"}
NEGATIVE = {"hate", "bad", "sad", "terrible", "awful", "horrible", "worst"}

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    text = payload.text.lower()

    score = 0
    for word in POSITIVE:
        if word in text:
            score += 1
    for word in NEGATIVE:
        if word in text:
            score -= 1

    if score > 0:
        return {"label": "positive", "score": 1.0}
    elif score < 0:
        return {"label": "negative", "score": 1.0}
    else:
        return {"label": "neutral", "score": 0.5}
