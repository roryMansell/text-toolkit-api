from fastapi import FastAPI
from app.routers import health, clean, sentiment, similarity
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Text Toolkit API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later lock down to your frontend origin
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(health.router)
app.include_router(clean.router)
app.include_router(sentiment.router)
app.include_router(similarity.router)
