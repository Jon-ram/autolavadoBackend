import models.model_usuario_vehiculo_servicio
import schemas.schema_usuario_vehiculo_servicio
from sqlalchemy.orm import Session

def get_usuario_vehiculo_servicio(db: Session, skip: int = 0, limit: int = 10):
    '''Función para obtener un usuario_vehiculo_servicio por su ID'''
    return db.query(models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio).offset(skip).limit(limit).all()

def create_usuario_vehiculo_servicio(db: Session, usuario_vehiculo_servicio: schemas.schema_usuario_vehiculo_servicio.Usuario_Vehiculo_ServicioCreate):
    '''Función para crear un nuevo usuario_vehiculo_servicio'''
    db_usuario_vehiculo_servicio = models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio(
        usuario_Id=usuario_vehiculo_servicio.usuario_Id,
        vehiculo_Id=usuario_vehiculo_servicio.vehiculo_Id,
        servicio_Id=usuario_vehiculo_servicio.servicio_Id,
        fecha_registro=usuario_vehiculo_servicio.fecha_registro
    )
    db.add(db_usuario_vehiculo_servicio)
    db.commit()
    db.refresh(db_usuario_vehiculo_servicio)
    return db_usuario_vehiculo_servicio

def update_usuario_vehiculo_servicio(db: Session, usuario_vehiculo_servicio_id: int, usuario_vehiculo_servicio: schemas.schema_usuario_vehiculo_servicio.Usuario_Vehiculo_ServicioUpdate):
    '''Función para actualizar un usuario_vehiculo_servicio existente'''
    db_usuario_vehiculo_servicio = db.query(models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio).filter(models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio.Id == usuario_vehiculo_servicio_id).first()
    if db_usuario_vehiculo_servicio is None:
        return None
    db_usuario_vehiculo_servicio.usuario_Id = usuario_vehiculo_servicio.usuario_Id
    db_usuario_vehiculo_servicio.vehiculo_Id = usuario_vehiculo_servicio.vehiculo_Id
    db_usuario_vehiculo_servicio.servicio_Id = usuario_vehiculo_servicio.servicio_Id
    db_usuario_vehiculo_servicio.fecha_registro = usuario_vehiculo_servicio.fecha_registro
    db.commit()
    db.refresh(db_usuario_vehiculo_servicio)
    return db_usuario_vehiculo_servicio

def delete_usuario_vehiculo_servicio(db: Session, usuario_vehiculo_servicio_id: int):
    '''Función para eliminar un usuario_vehiculo_servicio por su ID'''
    db_usuario_vehiculo_servicio = db.query(models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio).filter(models.model_usuario_vehiculo_servicio.Usuario_Vehiculo_Servicio.Id == usuario_vehiculo_servicio_id).first()
    if db_usuario_vehiculo_servicio is None:
        return None
    db.delete(db_usuario_vehiculo_servicio)
    db.commit()
    return db_usuario_vehiculo_servicio

