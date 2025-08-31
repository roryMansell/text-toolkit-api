from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)

def test_sentiment_labels():
    r = c.post("/sentiment", json={"text": "this is great and wonderful"})
    assert r.status_code == 200
    assert r.json()["label"] in {"positive", "negative"}
