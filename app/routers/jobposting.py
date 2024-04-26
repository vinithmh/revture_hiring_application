from fastapi import APIRouter, Depends, FastAPI, HTTPException, Header
from ..schemas import User, UserRoleEnum
from ..oauth2 import get_current_user, get_current_active_user

router = APIRouter(
    tags=["Job Postings"],
)

@router.get("/job-postings", response_model=User)
async def create_job_posting(
    token: str = Header(...),  # Retrieve token from the request headers
    current_user: User = Depends(get_current_user),
):
    current_user = await get_current_active_user(current_user, UserRoleEnum.employer)
    return current_user