'''
Docstring for schemas.schema_usuario_vehiculo_servicio
'''
from datetime import datetime,date,time
from pydantic import BaseModel

class UsuarioVehiculoServicioBase(BaseModel):
    '''Clase para modelar los campos de tabla Usuario_Vehiculo_Servicio'''
    cajero_id: int
    lavador_id: int
    servicio_id: int
    vehiculo_id: int
    fecha: date
    hora: time
    estado: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime
# pylint: disable=too-few-public-methods, unnecessary-pass
class UsuarioVehiculoServicioCreate(UsuarioVehiculoServicioBase):
    '''Clase para asignar un servicio a un vehiculo'''
    pass
class UsuarioVehiculoServicioUpdate(UsuarioVehiculoServicioBase):
    '''Clase para actualizar un servicio a un vehiculo'''
    pass
class UsuarioVehiculoServicio(UsuarioVehiculoServicioBase):
    '''Clase para realizar operaciones por ID en tabla Usuario_Vehiculo_Servicio'''
    Id: int
    class Config:
        '''Utilizar el orm para ejecutar las funcionalidades'''
        orm_mode =True