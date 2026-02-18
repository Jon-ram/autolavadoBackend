'''
Docstring for models.modelUser
'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    ''' Docstring for User'''
    __tablename__ = "tbb_users"
    Id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("tbc_roles.Id"))
    nombre = Column(String(60))
    papellido = Column(String(60))
    sapellido = Column(String(60))
    direccion = Column(String(100))
    correo_electronico = Column(String(60))
    numero_telefono = Column(String(10)) 
    contrasena = Column(String(255))  
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)

    rol = relationship("Rols", back_populates="user")
    vehiculo = relationship("Vehiculo", back_populates="Vehiculo")
    cajero = relationship("ServicioVehiculo", foreign_keys="ServicioVehiculo.cajero_Id", back_populates="cajero")
    lavador = relationship("ServicioVehiculo", foreign_keys="ServicioVehiculo.lavador_Id", back_populates="lavador")