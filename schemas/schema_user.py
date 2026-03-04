from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserBase(BaseModel):
    '''Esquema base para usuarios'''
    rol_Id: int
    nombre: str = Field(..., max_length=60)
    papellido: str = Field(..., max_length=60)
    sapellido: Optional[str] = Field(None, max_length=60)
    direccion: Optional[str] = Field(None, max_length=100)
    correo_electronico: EmailStr
    numero_telefono: str = Field(..., pattern=r"^\d{10}$")
    estatus: bool = True

class UserCreate(UserBase):
    '''Esquema para crear usuario'''
    contrasena: str = Field(..., min_length=6)
    
    @field_validator('contrasena')
    @classmethod
    def validate_password_length(cls, v):
        # Verificar bytes, no caracteres (límite de bcrypt)
        if len(v.encode('utf-8')) > 72:
            raise ValueError('La contraseña no puede exceder 72 bytes cuando se codifica en UTF-8')
        return v

class UserUpdate(BaseModel):
    '''Esquema para actualizar usuario'''
    rol_Id: Optional[int] = None
    nombre: Optional[str] = Field(None, max_length=60)
    papellido: Optional[str] = Field(None, max_length=60)
    sapellido: Optional[str] = Field(None, max_length=60)
    direccion: Optional[str] = Field(None, max_length=100)
    correo_electronico: Optional[EmailStr] = None
    numero_telefono: Optional[str] = Field(None, pattern=r"^\d{10}$")
    contrasena: Optional[str] = Field(None, min_length=6)
    
    @field_validator('contrasena')
    @classmethod
    def validate_password_length(cls, v):
        if v and len(v.encode('utf-8')) > 72:
            raise ValueError('La contraseña no puede exceder 72 bytes cuando se codifica en UTF-8')
        return v

class UserLogin(BaseModel):
    '''Esquema para login'''
    correo_electronico: Optional[EmailStr] = None
    numero_telefono: Optional[str] = Field(None, pattern=r"^\d{10}$")
    contrasena: str

class Token(BaseModel):
    '''Esquema para el token JWT'''
    access_token: str
    token_type: str

class User(UserBase):
    '''Esquema para respuesta de usuario'''
    Id: int
    fecha_registro: datetime
    fecha_modificacion: Optional[datetime] = None

    class Config:
        from_attributes = True