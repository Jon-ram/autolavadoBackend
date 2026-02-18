'''
Docstring for models.vehiculos
'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
class Vehiculo(Base):
    ''' Docstring for Vehiculo'''
    __tablename__ = "tbb_vehiculo"
    Id = Column(Integer, primary_key=True, index=True)
    usuario_Id = Column(Integer, ForeignKey("tbb_users.Id"))
    placa = Column(String(15))
    serie = Column(String(60))
    modelo = Column(String(60))
    color = Column(String(60))
    tipo = Column(String(60))
    anio = Column(Integer)
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)

    Vehiculo = relationship("User", back_populates="vehiculo")