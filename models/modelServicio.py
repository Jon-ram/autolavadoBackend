from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Servicio(Base):
    '''Modelo para la tabla de servicios'''
    __tablename__ = "tbc_servicio"
    
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(60), nullable=False)
    descripcion = Column(String(60))
    costo = Column(Float, nullable=False)
    duracion_minutos = Column(Integer)
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, onupdate=func.now())

    # Relaciones
    vehiculos_servicios = relationship("ServicioVehiculo", back_populates="servicio")