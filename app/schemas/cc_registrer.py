from pydantic import BaseModel

class CcRegistrerSchema(BaseModel):
    nombre : str
    apellido : str
    cedula : int
    time : str
