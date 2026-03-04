import os
from dotenv import load_dotenv
from fastapi.security import APIKeyHeader
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

load_dotenv()

# Esquema para el token JWT en el header
api_key_scheme = APIKeyHeader(name="Authorization", auto_error=False)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Crea un JSON Web Token (JWT) firmado."""
    to_encode = data.copy()
    
    # Calcular tiempo de expiración
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        expire = datetime.utcnow() + timedelta(minutes=expire_minutes)
    
    # Añadir el 'claim' de expiración
    to_encode.update({"exp": expire})
    
    # Codificar y firmar el token
    encoded_jwt = jwt.encode(
        to_encode, 
        os.getenv("SECRET_KEY"), 
        algorithm=os.getenv("ALGORITHM", "HS256")
    )
    return encoded_jwt

def get_current_user(token: str = Depends(api_key_scheme)):
    """Valida el token JWT y retorna el usuario (email/teléfono)"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Limpiar el token si viene con "Bearer "
        if token and token.startswith("Bearer "):
            token = token.split(" ")[1]
        
        # Decodificar el token
        payload = jwt.decode(
            token, 
            os.getenv("SECRET_KEY"), 
            algorithms=[os.getenv("ALGORITHM", "HS256")]
        )
        
        # Obtener el subject (email/teléfono)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
        
    except (JWTError, IndexError, AttributeError, ValueError):
        raise credentials_exception