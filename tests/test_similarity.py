from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)

def test_similarity_range():
    r = c.post("/similarity", json={"a": "I like apples", "b": "I enjoy apples"})
    assert r.status_code == 200
    sim = r.json()["similarity"]
    assert 0.0 <= sim <= 1.0
