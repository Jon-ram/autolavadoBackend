import models.modelUser
import schemas.schema_user
from sqlalchemy.orm import Session

def get_user(db: Session, skip: int = 0, limit: int = 10):
    '''Función para obtener un usuario por su ID'''
    return db.query(models.modelUser.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.schema_user.UserCreate):
    '''Función para crear un nuevo usuario'''
    db_user = models.modelUser.User(
        nombre_usuario=user.nombre_usuario,
        correo_usuario=user.correo_usuario,
        contraseña_usuario=user.contraseña_usuario,
        estado=user.estado
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.schema_user.UserUpdate):
    '''Función para actualizar un usuario existente'''
    db_user = db.query(models.modelUser.User).filter(models.modelUser.User.Id == user_id).first()
    if db_user is None:
        return None
    db_user.nombre_usuario = user.nombre_usuario
    db_user.correo_usuario = user.correo_usuario
    db_user.contraseña_usuario = user.contraseña_usuario
    db_user.estado = user.estado
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    '''Función para eliminar un usuario por su ID'''
    db_user = db.query(models.modelUser.User).filter(models.modelUser.User.Id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user

