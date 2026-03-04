from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class ServicioBase(BaseModel):
    '''Esquema base para servicios'''
    nombre: str = Field(..., max_length=60)
    descripcion: Optional[str] = Field(None, max_length=60)
    costo: float = Field(..., gt=0)
    duracion_minutos: int = Field(..., gt=0)
    estado: bool = True

class ServicioCreate(ServicioBase):
    '''Esquema para crear servicio'''
    pass

class ServicioUpdate(BaseModel):
    '''Esquema para actualizar servicio'''
    nombre: Optional[str] = Field(None, max_length=60)
    descripcion: Optional[str] = Field(None, max_length=60)
    costo: Optional[float] = Field(None, gt=0)
    duracion_minutos: Optional[int] = Field(None, gt=0)
    estado: Optional[bool] = None

class Servicio(ServicioBase):
    '''Esquema para respuesta de servicio'''
    Id: int
    fecha_registro: datetime
    fecha_modificacion: Optional[datetime] = None

    class Config:
        from_attributes = True