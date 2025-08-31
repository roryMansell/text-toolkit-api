from fastapi import FastAPI
from app.routers import health, clean, sentiment, similarity

app = FastAPI(title="Text Toolkit API", version="0.1.0")
app.include_router(health.router)
app.include_router(clean.router)
app.include_router(sentiment.router)
app.include_router(similarity.router)
