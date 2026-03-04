from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class RolBase(BaseModel):
    '''Esquema base para roles'''
    nombre_rol: str = Field(..., max_length=15)
    estado: bool = True

class RolCreate(RolBase):
    '''Esquema para crear un rol'''
    pass

class RolUpdate(BaseModel):
    '''Esquema para actualizar un rol'''
    nombre_rol: Optional[str] = Field(None, max_length=15)
    estado: Optional[bool] = None

class Rol(RolBase):
    '''Esquema para respuesta de rol'''
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True