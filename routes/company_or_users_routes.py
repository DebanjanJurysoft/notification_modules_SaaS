from fastapi import APIRouter, Depends, Header, HTTPException, Path
from typing import Annotated

router = APIRouter()


@router.post('/register-user')
async def register_users(authorization: Annotated[str | None, Header()]):
    if authorization is None:
        raise HTTPException(status_code=401, detail='Authorization header is required')
    return fetch_my_wallet(authorization)
