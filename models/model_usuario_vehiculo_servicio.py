from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Time, ForeignKey
from enum import Enum
from config.db import Base

class Solicitud():
    Programada = "Programada" 
    Proceso = "Proceso"
    Realizada = "Realizada"
    Cancelada = "Cancelada"

class VehiculosServicio(Base):
    _tablemname_ = "tbd_usuario_vehiculo_servicio"
    Id = Column(Integer, primary_key=True, index=True)
    vehiculo_Id = Column(Integer, ForeignKey("tbb_vehiculos"))
    cajero_Id = Column()
    lavador_Id = Column()
    servicio_Id = Column()
    fecha = Column()
    hora = Column()
    estatus = Column()
    estado = Column()
    fecha_registro = Column()
    fecha_actualizacion = Column()
