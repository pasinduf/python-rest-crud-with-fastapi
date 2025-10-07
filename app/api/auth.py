from fastapi import APIRouter
from fastapi.params import Depends
from app.core.database import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from sqlalchemy.orm import Session
from app.crud import auth


router = APIRouter()

@router.post("/login/",response_model=LoginResponse)
def login(payload:LoginRequest, db:Session = Depends(get_db)):
    return auth.login(db, payload)