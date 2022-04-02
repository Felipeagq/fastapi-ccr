from dotenv import load_dotenv
import os

from pydantic import BaseSettings, HttpUrl
from typing import Union,Any
from datetime import datetime, timedelta

from passlib.context import CryptContext
from jose import jwt


BASE_DIR = os.path.abspath(os.curdir)

class Settings(BaseSettings):
    SECRET_KET: str = os.urandom(12).hex()
    SQLALCHEMY_DATABASE_URL: str = f"sqlite:///{BASE_DIR}/database.db"

    PROJECT_NAME: str = "CC Scanner"
    PROJECT_VERSION: str = "v0.0.1"
    API_V1_STR: str = "/api/v1"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 3
    ALGORITHMS: str = "HS256"
    BACKEND_CORS_ORIGINS: list[HttpUrl] = []


settings = Settings()

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    subject: Union[str,Any],
    expire_delta: timedelta = None 
) -> str:
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "expire" : expire,
        "subject": str(subject)
    }
    return jwt.encode(
        to_encode,
        settings.SECRET_KET,
        algorithm = settings.ALGORITHMS
    )


def verify_password(
    plain_password: str,
    hashed_password: str
) -> str:
    return password_context.verify(
        plain_password,
        hashed_password
    )


def get_password(
    password: str
) -> str:
    return password_context.hash(password)