from fastapi import APIRouter, Body

from app.services.summarize_service import summarize_text

router = APIRouter()

@router.post("/summarize")
async def summarize(text: str = Body(..., embed=True)):
    summary = summarize_text(text)
    return {"summary": summary}
