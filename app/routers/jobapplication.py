from fastapi import APIRouter, Depends, FastAPI, HTTPException, Header
from ..schemas import User, UserRoleEnum
from ..oauth2 import get_current_user, get_current_active_user

router = APIRouter(
    tags=["Job Applications"],
)

@router.get("/job-applications", response_model=User)
async def apply_for_job(
    token: str = Header(...),  # Retrieve token from the request headers
    current_user: User = Depends(get_current_user),
):
    current_user = await get_current_active_user(current_user, UserRoleEnum.job_seeker)
    return current_user