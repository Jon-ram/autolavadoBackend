'''
Docstring for models.servicio
'''
from sqlalchemy import Column, Integer, String, Boolean, Float,DateTime 

from config.db import Base
class Servicio(Base):
    ''' Docstring for Servicio'''
    __tablename__ = "tbc_servicio"
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60))
    descripcion = Column(String(60))
    costo = Column(Float)
    duracion_minutos = Column(Integer)
    estado = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)