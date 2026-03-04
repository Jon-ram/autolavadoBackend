from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Vehiculo(Base):
    '''Modelo para la tabla de vehículos'''
    __tablename__ = "tbb_vehiculo"
    
    Id = Column(Integer, primary_key=True, index=True)
    usuario_Id = Column(Integer, ForeignKey("tbb_users.Id"))
    placa = Column(String(15), unique=True)
    serie = Column(String(60))
    modelo = Column(String(60))
    color = Column(String(60))
    tipo = Column(String(60))
    anio = Column(Integer)
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, onupdate=func.now())

    # Relaciones
    usuario = relationship("User", back_populates="vehiculos")
    servicios = relationship("ServicioVehiculo", back_populates="vehiculo")