from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import config.db, models.modelRols, schemas.schema_rols, crud.crud_rols 

rol_router = APIRouter()

models.modelRols.Base.metadata.create_all(bind=config.db.engine)    

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol_router.get("/rol/", response_model=list[schemas.schema_rols.Rol], tags=["Rols"])        
async def read_rols(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    '''Función para obtener un rol por su ID'''
    db_rol = crud.crud_rols.get_rol(db, skip=skip, limit=limit)
    return db_rol

@rol_router.post("/rol/", response_model=schemas.schema_rols.Rol, tags=["Rols"])
async def create_rol(rol: schemas.schema_rols.RolCreate, db: Session = Depends(get_db)):
    '''Función para crear un nuevo rol'''
    db_rol = crud.crud_rols.create_rol(db=db, rol=rol)
    return db_rol

@rol_router.delete("/rol/{rol_id}", tags=["Rols"])
async def delete_rol(rol_id: int, db: Session = Depends(get_db)):
    '''Función para eliminar un rol por su ID'''
    db_rol = crud.crud_rols.delete_rol(db=db, rol_id=rol_id)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return {"detail": "Rol eliminado exitosamente"}

@rol_router.put("/rol/{rol_id}", response_model=schemas.schema_rols.Rol, tags=["Rols"])
async def update_rol(rol_id: int, rol: schemas.schema_rols.RolUpdate, db: Session = Depends(get_db)):
    '''Función para actualizar un rol por su ID'''
    db_rol = crud.crud_rols.update_rol(db=db, rol_id=rol_id, rol=rol)
    if db_rol is None:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol