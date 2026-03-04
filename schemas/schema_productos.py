from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class ProductoBase(BaseModel):
    '''Esquema base para productos'''
    nombre: str = Field(..., max_length=100)
    descripcion: Optional[str] = Field(None, max_length=200)
    precio: float = Field(..., gt=0)
    stock: int = Field(0, ge=0)
    categoria: Optional[str] = Field(None, max_length=50)
    estado: bool = True

class ProductoCreate(ProductoBase):
    '''Esquema para crear producto'''
    pass

class ProductoUpdate(BaseModel):
    '''Esquema para actualizar producto'''
    nombre: Optional[str] = Field(None, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=200)
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    categoria: Optional[str] = Field(None, max_length=50)
    estado: Optional[bool] = None

class Producto(ProductoBase):
    '''Esquema para respuesta de producto'''
    Id: int
    fecha_registro: datetime
    fecha_modificacion: Optional[datetime] = None

    class Config:
        from_attributes = True