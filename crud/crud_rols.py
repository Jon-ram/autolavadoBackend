from sqlalchemy.orm import Session
from models.modelRols import Rols
from schemas import schema_rols

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener todos los roles'''
    return db.query(Rols).offset(skip).limit(limit).all()

def get_rol(db: Session, rol_id: int):
    '''Obtener un rol por ID'''
    return db.query(Rols).filter(Rols.Id == rol_id).first()

def create_rol(db: Session, rol: schema_rols.RolCreate):
    '''Crear un nuevo rol'''
    db_rol = Rols(**rol.dict())
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: schema_rols.RolUpdate):
    '''Actualizar un rol existente'''
    db_rol = get_rol(db, rol_id)
    if db_rol:
        update_data = rol.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_rol, key, value)
        db.commit()
        db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    '''Eliminar un rol por ID'''
    db_rol = get_rol(db, rol_id)
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol