from asyncore import read
from fastapi import APIRouter
api_router = APIRouter()

from app.routes import cc_post
api_router.include_router(cc_post.router, tags=["Include person to Database"])

from app.routes import read_cc
api_router.include_router(read_cc.router, tags=["Read database"])