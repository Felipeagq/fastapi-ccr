from fastapi import APIRouter,Depends, status

from app.database.database import get_db
from sqlalchemy.orm import Session
from app.database.models.cc_registrer import CcRegistrerDDBB

from app.schemas.cc_registrer import CcRegistrerSchema


router = APIRouter()

@router.post("/add-cc", status_code= status.HTTP_201_CREATED)
def add_cc(
    persona: CcRegistrerSchema,
    db: Session = Depends(get_db) 
):
    new_persona = CcRegistrerDDBB(
        nombre = persona.nombre,
        apellido= persona.apellido,
        cedula= persona.cedula,
        time= persona.time
    )
    db.add(new_persona)
    db.commit()
    db.refresh(new_persona)
    return {
        "msg": "ok",
        "Persona": new_persona
    }
