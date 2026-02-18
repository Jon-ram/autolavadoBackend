'''
Docstring for models.model_usuario_vehiculo_servicio.
Esta Clase permite generar el modelo para las ventas y asignaciones
'''

from sqlalchemy import Column, Integer, Boolean, DateTime, Date, Time, ForeignKey, Enum
from enum import Enum as PyEnum
from sqlalchemy.orm import relationship
from config.db import Base


class Solicitud(str, PyEnum):
    '''
    Clase para especificar estatus de solicitud
    '''
    Programa = "Programa"
    Proceso = "Proceso"
    Realizada = "Realizada"
    Cancelada = "Cancelada"


class ServicioVehiculo(Base):
    '''Clase para especificar tabla usuario_vehiculo_servicio'''

    __tablename__ = "tbd_usuario_vehiculo_servicio"

    Id = Column(Integer, primary_key=True, index=True)
    cajero_Id = Column(Integer, ForeignKey("tbb_users.Id"))
    lavador_Id = Column(Integer, ForeignKey("tbb_users.Id"))
    servicio_Id = Column(Integer, ForeignKey("tbc_servicio.Id"))
    vehiculo_Id = Column(Integer, ForeignKey("tbb_vehiculo.Id"))

    fecha = Column(Date)
    hora = Column(Time)
    estatus = Column(Enum(Solicitud))
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_actualizacion = Column(DateTime)

    cajero = relationship("User", foreign_keys=[cajero_Id])
    lavador = relationship("User", foreign_keys=[lavador_Id])