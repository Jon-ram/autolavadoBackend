from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_usuario_vehiculo_servicio
from schemas import schema_usuario_vehiculo_servicio
from config.security import get_current_user

servicio_vehiculo_router = APIRouter(prefix="/servicios-vehiculo", tags=["Servicios por Vehículo"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@servicio_vehiculo_router.get("/", response_model=List[schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio])
async def read_servicios_vehiculo(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los servicios de vehículos (requiere autenticación)'''
    servicios = crud_usuario_vehiculo_servicio.get_servicios_vehiculo(db=db, skip=skip, limit=limit)
    return servicios

@servicio_vehiculo_router.get("/{servicio_id}", response_model=schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio)
async def read_servicio_vehiculo(
    servicio_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un servicio de vehículo por ID (requiere autenticación)'''
    db_servicio = crud_usuario_vehiculo_servicio.get_servicio_vehiculo(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicio_vehiculo_router.get("/vehiculo/{vehiculo_id}", response_model=List[schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio])
async def read_servicios_by_vehiculo(
    vehiculo_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener servicios por vehículo (requiere autenticación)'''
    servicios = crud_usuario_vehiculo_servicio.get_servicios_by_vehiculo(db=db, vehiculo_id=vehiculo_id)
    return servicios

@servicio_vehiculo_router.get("/lavador/{lavador_id}", response_model=List[schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio])
async def read_servicios_by_lavador(
    lavador_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener servicios por lavador (requiere autenticación)'''
    servicios = crud_usuario_vehiculo_servicio.get_servicios_by_lavador(db=db, lavador_id=lavador_id)
    return servicios

@servicio_vehiculo_router.get("/cajero/{cajero_id}", response_model=List[schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio])
async def read_servicios_by_cajero(
    cajero_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener servicios por cajero (requiere autenticación)'''
    servicios = crud_usuario_vehiculo_servicio.get_servicios_by_cajero(db=db, cajero_id=cajero_id)
    return servicios

@servicio_vehiculo_router.post("/", response_model=schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio, status_code=status.HTTP_201_CREATED)
async def create_servicio_vehiculo(
    servicio: schema_usuario_vehiculo_servicio.UsuarioVehiculoServicioCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Crear un nuevo servicio de vehículo (requiere autenticación)'''
    return crud_usuario_vehiculo_servicio.create_servicio_vehiculo(db=db, servicio=servicio)

@servicio_vehiculo_router.put("/{servicio_id}", response_model=schema_usuario_vehiculo_servicio.UsuarioVehiculoServicio)
async def update_servicio_vehiculo(
    servicio_id: int, 
    servicio: schema_usuario_vehiculo_servicio.UsuarioVehiculoServicioUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un servicio de vehículo existente (requiere autenticación)'''
    db_servicio = crud_usuario_vehiculo_servicio.update_servicio_vehiculo(
        db=db, servicio_id=servicio_id, servicio=servicio
    )
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return db_servicio

@servicio_vehiculo_router.delete("/{servicio_id}")
async def delete_servicio_vehiculo(
    servicio_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un servicio de vehículo por ID (requiere autenticación)'''
    db_servicio = crud_usuario_vehiculo_servicio.delete_servicio_vehiculo(db=db, servicio_id=servicio_id)
    if db_servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"message": "Servicio eliminado exitosamente"}