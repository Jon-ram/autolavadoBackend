from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_rols
from schemas import schema_rols
from config.security import get_current_user

rol_router = APIRouter(prefix="/roles", tags=["Roles"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints públicos (NO requieren token)
@rol_router.post("/", response_model=schema_rols.Rol, status_code=status.HTTP_201_CREATED)
async def create_rol(rol: schema_rols.RolCreate, db: Session = Depends(get_db)):
    '''Crear un nuevo rol (público - no requiere autenticación)'''
    return crud_rols.create_rol(db=db, rol=rol)

# Endpoints protegidos (SÍ requieren token)
@rol_router.get("/", response_model=List[schema_rols.Rol])
async def read_roles(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los roles (requiere autenticación)'''
    roles = crud_rols.get_roles(db, skip=skip, limit=limit)
    return roles

@rol_router.get("/{rol_id}", response_model=schema_rols.Rol)
async def read_rol(
    rol_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un rol por ID (requiere autenticación)'''
    db_rol = crud_rols.get_rol(db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol

@rol_router.put("/{rol_id}", response_model=schema_rols.Rol)
async def update_rol(
    rol_id: int, 
    rol: schema_rols.RolUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un rol existente (requiere autenticación)'''
    db_rol = crud_rols.update_rol(db=db, rol_id=rol_id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol

@rol_router.delete("/{rol_id}")
async def delete_rol(
    rol_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un rol por ID (requiere autenticación)'''
    db_rol = crud_rols.delete_rol(db=db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"message": "Rol eliminado exitosamente"}