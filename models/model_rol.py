'''Esta calse permite generar el modelo para los tipos de Rols'''
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from config.db import Base

class Rols(Base):
    __tablename__ = "tbc_rols"
    id = Column(Integer, primary_key=True, index=True)
    rol_Id = Column(Integer, ForeignKey("tbc_rols.id"))
    nombre = Column(String(60))
    papellido = Column(String(60))
    sapellido = Column(String(60))
    usuario = Column(String(60))
    contrasena = Column(String(60))
    telefono = Column(String(60))
    estatus = Column(Boolean)
    fecha_registro = Column(DateTime)
    fecha_modificacion = Column(DateTime)
