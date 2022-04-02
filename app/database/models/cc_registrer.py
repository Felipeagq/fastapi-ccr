from email.mime import base
from sqlalchemy import Column, String, Integer
from app.database.database import Base

class CcRegistrerDDBB(Base):
    __tablename__ = "Cc_Registrer"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    apellido = Column(String)
    cedula = Column(Integer)
    time = Column(String)