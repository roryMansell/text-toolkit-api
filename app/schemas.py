from pydantic import BaseModel, Field

class TextIn(BaseModel):
    text: str = Field(min_length=1)

class PairIn(BaseModel):
    a: str = Field(min_length=1)
    b: str = Field(min_length=1)

class CleanOut(BaseModel):
    cleaned: str

class SentimentOut(BaseModel):
    label: str
    score: float  # 0..1

class SimilarityOut(BaseModel):
    similarity: float  # 0..1
