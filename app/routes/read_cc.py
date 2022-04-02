from fastapi import APIRouter, status, Depends,HTTPException

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


@router.get("/read_cc/{cc}", status_code=status.HTTP_302_FOUND )
def find_cc(
    cc:int,
    db: Session = Depends(get_db)
) -> str:
    persona = db.query(CcRegistrerDDBB).filter(CcRegistrerDDBB.cedula == cc).first()
    if not persona: 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "person not found"
        )
    return {
        "msg":"ok",
        "persona": persona
    }