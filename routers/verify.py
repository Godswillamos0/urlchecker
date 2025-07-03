from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from .utilis import analyze_url



router = APIRouter(
    prefix="/verify",
    tags=["verify"]
)


class UrlRequest(BaseModel):
    url: str = Field(max_length=150)


@router.post('/', status_code=status.HTTP_200_OK)
def get_if_url_verified(request: UrlRequest):
    result = analyze_url(request.url)
    return result
