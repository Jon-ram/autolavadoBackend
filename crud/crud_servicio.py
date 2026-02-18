import models.modelServicio
import schemas.schema_servicio
from sqlalchemy.orm import Session

def get_servicio(db: Session, skip: int = 0, limit: int = 10):
    '''Función para obtener un servicio por su ID'''
    return db.query(models.modelServicio.Servicio).offset(skip).limit(limit).all()

def create_servicio(db: Session, servicio: schemas.schema_servicio.ServicioCreate):
    '''Función para crear un nuevo servicio'''
    db_servicio = models.modelServicio.Servicio(
        nombre_servicio=servicio.nombre_servicio,
        descripcion=servicio.descripcion,
        precio=servicio.precio,
        estado=servicio.estado
    )
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, servicio_id: int, servicio: schemas.schema_servicio.ServicioUpdate):
    '''Función para actualizar un servicio existente'''
    db_servicio = db.query(models.modelServicio.Servicio).filter(models.modelServicio.Servicio.Id == servicio_id).first()
    if db_servicio is None:
        return None
    db_servicio.nombre_servicio = servicio.nombre_servicio
    db_servicio.descripcion = servicio.descripcion
    db_servicio.precio = servicio.precio
    db_servicio.estado = servicio.estado
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, servicio_id: int):
    '''Función para eliminar un servicio por su ID'''
    db_servicio = db.query(models.modelServicio.Servicio).filter(models.modelServicio.Servicio.Id == servicio_id).first()
    if db_servicio is None:
        return None
    db.delete(db_servicio)
    db.commit()
    return db_servicio
