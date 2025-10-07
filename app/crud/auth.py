from app.core.bycrypt import verify_password
from app.core.jwt import generate_access_token
from app.models.user import User
from app.schemas.auth import LoginRequest
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.core.logger import logger

def login(db:Session, payload:LoginRequest):
    try:
        user = User.active(db.query(User).filter(User.username == payload.username)).first()
        if not user or not verify_password(payload.password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = generate_access_token({"sub": user.username, "first_name": user.firstName, "last_name": user.lastName})
        return {"success": True, "message": "Login successful", "token": token}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to login: {e}")
        raise HTTPException(status_code=500, detail="Failed to login.")