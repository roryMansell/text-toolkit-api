from pydantic import BaseModel, Field
from typing import Literal


class TextIn(BaseModel):
    text: str = Field(min_length=1)

class PairIn(BaseModel):
    a: str = Field(min_length=1)
    b: str = Field(min_length=1)

class CleanOut(BaseModel):
    cleaned: str

class SentimentOut(BaseModel):
    label: Literal["positive", "neutral", "negative"]
    score: float  # 0..1

class SimilarityOut(BaseModel):
    similarity: float  # 0..1
