from fastapi import APIRouter, status, Depends

from sqlalchemy.orm import Session
from app.database.models.cc_registrer import CcRegistrerDDBB
from app.database.database import get_db

router = APIRouter()

@router.get("/read_cc", status_code=status.HTTP_200_OK)
def read_cc(
    db: Session = Depends(get_db)
) -> str:
    personas = db.query(CcRegistrerDDBB).all()
    return personas