from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)

def test_clean_basic():
    r = c.post("/clean", json={"text": "  HELLO   world  "})
    assert r.status_code == 200
    assert r.json()["cleaned"] == "hello world"
