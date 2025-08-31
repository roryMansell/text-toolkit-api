import re
from fastapi import APIRouter
from app.schemas import TextIn, CleanOut

router = APIRouter(prefix="/clean", tags=["text"])
_ws = re.compile(r"\s+")

@router.post("", response_model=CleanOut)
def clean(payload: TextIn):
    s = payload.text.strip().lower()
    s = _ws.sub(" ", s)
    return {"cleaned": s}
