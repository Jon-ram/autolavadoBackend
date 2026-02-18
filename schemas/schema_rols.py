'''Docstring for schema.schema_rols'''

from datetime import datetime
from pydantic import BaseModel




class RolBase(BaseModel):
    ''' Clase para modelar los campos de tabla Rols'''
    nombre: str
    estatus: bool
    fecha_registro: datetime
    fecha_actualizacion: datetime

#pylint: disable=too-few-public-methods, unnecessary-pass
class RolCreate(RolBase):
    ''' Clase para crear un Rol basado en la tabla Rols'''
    pass

class RolUpdate(RolBase):
    ''' Clase para actualizar un Rol basado en la tabla Rols'''
    pass

class Rol(RolBase):
    '''Clase para realizar operaciones por ID en la tabla Rol'''
    id: int
    class Config:
        '''Utilizar el omr para ejecutar las funcionalidades'''
        orm_mode = True