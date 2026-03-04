from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class Producto(Base):
    '''Modelo para la tabla de productos'''
    __tablename__ = "tbc_productos"
    
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(200))
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    categoria = Column(String(50))
    estado = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, onupdate=func.now())
    
    # Relaciones (si se usan en servicios)
    # productos_servicios = relationship("ServicioProducto", back_populates="producto")