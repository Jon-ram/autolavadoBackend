from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from config.db import Base

class User(Base):
    '''Modelo para la tabla de usuarios'''
    __tablename__ = "tbb_users"
    
    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"))
    nombre = Column(String(60), nullable=False)
    papellido = Column(String(60), nullable=False)
    sapellido = Column(String(60))
    direccion = Column(String(100))
    correo_electronico = Column(String(60), unique=True, index=True)
    numero_telefono = Column(String(10), unique=True) 
    contrasena = Column(String(255), nullable=False)  
    estatus = Column(Boolean, default=True)
    fecha_registro = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, onupdate=func.now())

    # Relaciones
    rol = relationship("Rols", back_populates="usuarios")
    vehiculos = relationship("Vehiculo", back_populates="usuario")
    cajero = relationship("ServicioVehiculo", foreign_keys="ServicioVehiculo.cajero_Id", back_populates="cajero_rel")
    lavador = relationship("ServicioVehiculo", foreign_keys="ServicioVehiculo.lavador_Id", back_populates="lavador_rel")