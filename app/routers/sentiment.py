from fastapi import APIRouter
from app.schemas import TextIn, SentimentOut

router = APIRouter(prefix="/sentiment", tags=["nlp"])

POS = {"good","great","love","excellent","happy","awesome","amazing","nice","wonderful"}
NEG = {"bad","terrible","hate","awful","sad","horrible","poor","worst","angry"}

def score_rule(text: str) -> float:
    words = {w.strip(".,!?;:").lower() for w in text.split()}
    pos = len(words & POS)
    neg = len(words & NEG)
    if pos == neg == 0:
        return 0.5
    total = pos + neg
    return (pos / total) if total else 0.5

@router.post("", response_model=SentimentOut)
def sentiment(payload: TextIn):
    s = score_rule(payload.text)
    label = "positive" if s >= 0.5 else "negative"
    return {"label": label, "score": float(s)}
