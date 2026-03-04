from sqlalchemy.orm import Session
from models.modelVehiculos import Vehiculo
from schemas import schema_vehiculos

def get_vehiculos(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener todos los vehículos'''
    return db.query(Vehiculo).offset(skip).limit(limit).all()

def get_vehiculo(db: Session, vehiculo_id: int):
    '''Obtener un vehículo por ID'''
    return db.query(Vehiculo).filter(Vehiculo.Id == vehiculo_id).first()

def get_vehiculos_by_usuario(db: Session, usuario_id: int):
    '''Obtener vehículos por usuario'''
    return db.query(Vehiculo).filter(Vehiculo.usuario_Id == usuario_id).all()

def get_vehiculo_by_placa(db: Session, placa: str):
    '''Obtener vehículo por placa'''
    return db.query(Vehiculo).filter(Vehiculo.placa == placa).first()

def create_vehiculo(db: Session, vehiculo: schema_vehiculos.VehiculoCreate):
    '''Crear un nuevo vehículo'''
    db_vehiculo = Vehiculo(**vehiculo.model_dump())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, vehiculo_id: int, vehiculo: schema_vehiculos.VehiculoUpdate):
    '''Actualizar un vehículo existente'''
    db_vehiculo = get_vehiculo(db, vehiculo_id)
    if db_vehiculo:
        update_data = vehiculo.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_vehiculo, key, value)
        db.commit()
        db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, vehiculo_id: int):
    '''Eliminar un vehículo por ID'''
    db_vehiculo = get_vehiculo(db, vehiculo_id)
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
    return db_vehiculo