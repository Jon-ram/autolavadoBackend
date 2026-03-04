from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Rols(Base):
    '''Modelo para la tabla de roles'''
    __tablename__ = "tbc_roles"
    
    Id = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String(15), nullable=False)
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_actualizacion = Column(DateTime, onupdate=func.now())

    # Relaciones
    usuarios = relationship("User", back_populates="rol")