from sys import prefix
from fastapi import FastAPI
from app.settings import settings

from app.database.database import Base,engine
from app.database.models.cc_registrer import CcRegistrerDDBB
from app.routes import api_router

from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title= settings.PROJECT_NAME,
    version= settings.PROJECT_VERSION
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins = [str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods = ["*"],
        allow_headers = ["*"],
    )

Base.metadata.create_all(engine)

app.include_router(api_router,prefix= settings.API_V1_STR)