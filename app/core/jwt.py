from app.core.constants import JWT_TOKEN_EXPIREIN, JWT_ALGORITHM, JWT_SECRET
import jwt
from datetime import datetime, timedelta

def generate_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(seconds=JWT_TOKEN_EXPIREIN)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token
