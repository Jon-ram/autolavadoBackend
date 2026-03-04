from datetime import datetime, date, time
from typing import Optional
from pydantic import BaseModel, Field
from models.model_usuario_vehiculo_servicio import Solicitud

class UsuarioVehiculoServicioBase(BaseModel):
    '''Esquema base para servicios de vehículos'''
    cajero_Id: int
    lavador_Id: int
    servicio_Id: int
    vehiculo_Id: int
    fecha: date
    hora: time
    estatus: Solicitud = Solicitud.Programa
    estado: bool = True

class UsuarioVehiculoServicioCreate(UsuarioVehiculoServicioBase):
    '''Esquema para crear servicio de vehículo'''
    pass

class UsuarioVehiculoServicioUpdate(BaseModel):
    '''Esquema para actualizar servicio de vehículo (todos opcionales)'''
    cajero_Id: Optional[int] = None
    lavador_Id: Optional[int] = None
    servicio_Id: Optional[int] = None
    vehiculo_Id: Optional[int] = None
    fecha: Optional[date] = None
    hora: Optional[time] = None
    estatus: Optional[Solicitud] = None
    estado: Optional[bool] = None

class UsuarioVehiculoServicio(UsuarioVehiculoServicioBase):
    '''Esquema para respuesta de servicio de vehículo'''
    Id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True