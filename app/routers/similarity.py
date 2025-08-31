from fastapi import APIRouter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.schemas import PairIn, SimilarityOut

router = APIRouter(prefix="/similarity", tags=["nlp"])
_vectorizer = TfidfVectorizer(min_df=1, stop_words="english")

@router.post("", response_model=SimilarityOut)
def similarity(payload: PairIn):
    X = _vectorizer.fit_transform([payload.a, payload.b])
    sim = cosine_similarity(X[0], X[1])[0, 0]
    return {"similarity": float(sim)}
