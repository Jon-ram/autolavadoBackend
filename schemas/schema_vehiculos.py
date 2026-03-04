from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class VehiculoBase(BaseModel):
    '''Esquema base para vehículos'''
    usuario_Id: int
    placa: str = Field(..., max_length=15)
    serie: str = Field(..., max_length=60)
    modelo: str = Field(..., max_length=60)
    color: str = Field(..., max_length=60)
    tipo: str = Field(..., max_length=60)
    anio: int = Field(..., ge=1900, le=datetime.now().year)
    estatus: bool = True

class VehiculoCreate(VehiculoBase):
    '''Esquema para crear vehículo'''
    pass

class VehiculoUpdate(BaseModel):
    '''Esquema para actualizar vehículo (todos opcionales)'''
    placa: Optional[str] = Field(None, max_length=15)
    serie: Optional[str] = Field(None, max_length=60)
    modelo: Optional[str] = Field(None, max_length=60)
    color: Optional[str] = Field(None, max_length=60)
    tipo: Optional[str] = Field(None, max_length=60)
    anio: Optional[int] = Field(None, ge=1900, le=datetime.now().year)
    estatus: Optional[bool] = None

class Vehiculo(VehiculoBase):
    '''Esquema para respuesta de vehículo'''
    Id: int
    fecha_registro: datetime
    fecha_modificacion: Optional[datetime] = None

    class Config:
        from_attributes = True