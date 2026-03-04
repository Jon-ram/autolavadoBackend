from sqlalchemy.orm import Session
from models.modelServicio import Servicio
from schemas import schema_servicio

def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener todos los servicios'''
    return db.query(Servicio).offset(skip).limit(limit).all()

def get_servicio(db: Session, servicio_id: int):
    '''Obtener un servicio por ID'''
    return db.query(Servicio).filter(Servicio.Id == servicio_id).first()

def create_servicio(db: Session, servicio: schema_servicio.ServicioCreate):
    '''Crear un nuevo servicio'''
    db_servicio = Servicio(**servicio.dict())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, servicio_id: int, servicio: schema_servicio.ServicioUpdate):
    '''Actualizar un servicio existente'''
    db_servicio = get_servicio(db, servicio_id)
    if db_servicio:
        update_data = servicio.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_servicio, key, value)
        db.commit()
        db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, servicio_id: int):
    '''Eliminar un servicio por ID'''
    db_servicio = get_servicio(db, servicio_id)
    if db_servicio:
        db.delete(db_servicio)
        db.commit()
    return db_servicio