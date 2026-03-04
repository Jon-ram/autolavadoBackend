from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_user
from schemas import schema_user
from config.security import create_access_token, get_current_user

usuario_router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario_router.get("/", response_model=List[schema_user.User])
async def read_usuarios(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los usuarios (requiere autenticación)'''
    usuarios = crud_user.get_usuarios(db=db, skip=skip, limit=limit)
    return usuarios

@usuario_router.get("/{usuario_id}", response_model=schema_user.User)
async def read_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un usuario por ID (requiere autenticación)'''
    db_usuario = crud_user.get_usuario(db=db, user_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@usuario_router.post("/", response_model=schema_user.User, status_code=status.HTTP_201_CREATED)
async def create_usuario(usuario: schema_user.UserCreate, db: Session = Depends(get_db)):
    '''Crear un nuevo usuario (NO requiere autenticación)'''
    # Verificar si el email ya existe
    db_usuario = crud_user.get_usuario_by_email(db, email=usuario.correo_electronico)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    # Verificar si el teléfono ya existe
    db_usuario = crud_user.get_usuario_by_telefono(db, telefono=usuario.numero_telefono)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Teléfono ya registrado")
    
    # Crear usuario
    nuevo_usuario = crud_user.create_usuario(db=db, usuario=usuario)
    if nuevo_usuario is None:
        raise HTTPException(status_code=400, detail="Error al crear usuario")
    
    return nuevo_usuario

@usuario_router.put("/{usuario_id}", response_model=schema_user.User)
async def update_usuario(
    usuario_id: int, 
    usuario: schema_user.UserUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un usuario existente (requiere autenticación)'''
    db_usuario = crud_user.update_usuario(db=db, user_id=usuario_id, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@usuario_router.delete("/{usuario_id}")
async def delete_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un usuario por ID (requiere autenticación)'''
    db_usuario = crud_user.delete_usuario(db=db, user_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado exitosamente"}

@usuario_router.post("/login", response_model=schema_user.Token)
async def login(login_data: schema_user.UserLogin, db: Session = Depends(get_db)):
    '''Login de usuario - devuelve token JWT'''
    user = crud_user.authenticate_user(db, login_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales incorrectas"
        )
    
    # Crear token JWT
    access_token = create_access_token(data={"sub": user.correo_electronico})
    return {"access_token": access_token, "token_type": "bearer"}