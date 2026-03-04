from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_vehiculos
from schemas import schema_vehiculos
from config.security import get_current_user

vehiculo_router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@vehiculo_router.get("/", response_model=List[schema_vehiculos.Vehiculo])
async def read_vehiculos(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los vehículos (requiere autenticación)'''
    vehiculos = crud_vehiculos.get_vehiculos(db=db, skip=skip, limit=limit)
    return vehiculos

@vehiculo_router.get("/{vehiculo_id}", response_model=schema_vehiculos.Vehiculo)
async def read_vehiculo(
    vehiculo_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un vehículo por ID (requiere autenticación)'''
    db_vehiculo = crud_vehiculos.get_vehiculo(db=db, vehiculo_id=vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return db_vehiculo

@vehiculo_router.get("/usuario/{usuario_id}", response_model=List[schema_vehiculos.Vehiculo])
async def read_vehiculos_by_usuario(
    usuario_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener vehículos por usuario (requiere autenticación)'''
    vehiculos = crud_vehiculos.get_vehiculos_by_usuario(db=db, usuario_id=usuario_id)
    return vehiculos

@vehiculo_router.post("/", response_model=schema_vehiculos.Vehiculo, status_code=status.HTTP_201_CREATED)
async def create_vehiculo(
    vehiculo: schema_vehiculos.VehiculoCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Crear un nuevo vehículo (requiere autenticación)'''
    # Verificar si la placa ya existe
    db_vehiculo = crud_vehiculos.get_vehiculo_by_placa(db, placa=vehiculo.placa)
    if db_vehiculo:
        raise HTTPException(status_code=400, detail="Placa ya registrada")
    
    return crud_vehiculos.create_vehiculo(db=db, vehiculo=vehiculo)

@vehiculo_router.put("/{vehiculo_id}", response_model=schema_vehiculos.Vehiculo)
async def update_vehiculo(
    vehiculo_id: int, 
    vehiculo: schema_vehiculos.VehiculoUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un vehículo existente (requiere autenticación)'''
    db_vehiculo = crud_vehiculos.update_vehiculo(db=db, vehiculo_id=vehiculo_id, vehiculo=vehiculo)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return db_vehiculo

@vehiculo_router.delete("/{vehiculo_id}")
async def delete_vehiculo(
    vehiculo_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un vehículo por ID (requiere autenticación)'''
    db_vehiculo = crud_vehiculos.delete_vehiculo(db=db, vehiculo_id=vehiculo_id)
    if db_vehiculo is None:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return {"message": "Vehículo eliminado exitosamente"}