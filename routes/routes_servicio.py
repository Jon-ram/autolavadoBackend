from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_servicio
from schemas import schema_servicio
from config.security import get_current_user

servicio_router = APIRouter(prefix="/servicios", tags=["Servicios"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@servicio_router.get("/", response_model=List[schema_servicio.Servicio])
async def read_servicios(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los servicios (requiere autenticación)'''
    servicios = crud_servicio.get_servicios(db=db, skip=skip, limit=limit)
    return servicios

@servicio_router.get("/{servicio_id}", response_model=schema_servicio.Servicio)
async def read_servicio(
    servicio_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un servicio por ID (requiere autenticación)'''
    db_servicio = crud_servicio.get_servicio(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicio_router.post("/", response_model=schema_servicio.Servicio, status_code=status.HTTP_201_CREATED)
async def create_servicio(
    servicio: schema_servicio.ServicioCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Crear un nuevo servicio (requiere autenticación)'''
    return crud_servicio.create_servicio(db=db, servicio=servicio)

@servicio_router.put("/{servicio_id}", response_model=schema_servicio.Servicio)
async def update_servicio(
    servicio_id: int, 
    servicio: schema_servicio.ServicioUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un servicio existente (requiere autenticación)'''
    db_servicio = crud_servicio.update_servicio(db=db, servicio_id=servicio_id, servicio=servicio)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicio_router.delete("/{servicio_id}")
async def delete_servicio(
    servicio_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un servicio por ID (requiere autenticación)'''
    db_servicio = crud_servicio.delete_servicio(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"message": "Servicio eliminado exitosamente"}