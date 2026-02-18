import models.modelVehiculos
import schemas.schema_vehiculos
from sqlalchemy.orm import Session

def get_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    '''Función para obtener un vehiculo por su ID'''
    return db.query(models.modelVehiculos.Vehiculo).offset(skip).limit(limit).all()

def create_vehiculo(db: Session, vehiculo: schemas.schema_vehiculos.VehiculoCreate):
    '''Función para crear un nuevo vehiculo'''
    db_vehiculo = models.modelVehiculos.Vehiculo(
        usuario_Id=vehiculo.usuario_Id,
        placa=vehiculo.placa,
        serie=vehiculo.serie,
        modelo=vehiculo.modelo,
        estado=vehiculo.estado
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, vehiculo_id: int, vehiculo: schemas.schema_vehiculos.VehiculoUpdate):
    '''Función para actualizar un vehiculo existente'''
    db_vehiculo = db.query(models.modelVehiculos.Vehiculo).filter(models.modelVehiculos.Vehiculo.Id == vehiculo_id).first()
    if db_vehiculo is None:
        return None
    db_vehiculo.usuario_Id = vehiculo.usuario_Id
    db_vehiculo.placa = vehiculo.placa
    db_vehiculo.serie = vehiculo.serie
    db_vehiculo.modelo = vehiculo.modelo
    db_vehiculo.estado = vehiculo.estado
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, vehiculo_id: int):
    '''Función para eliminar un vehiculo por su ID'''
    db_vehiculo = db.query(models.modelVehiculos.Vehiculo).filter(models.modelVehiculos.Vehiculo.Id == vehiculo_id).first()
    if db_vehiculo is None:
        return None
    db.delete(db_vehiculo)
    db.commit()
    return db_vehiculo
