from sqlalchemy.orm import Session
from models.model_usuario_vehiculo_servicio import ServicioVehiculo
from schemas import schema_usuario_vehiculo_servicio
from datetime import date

def get_servicios_vehiculo(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener todos los servicios de vehículos'''
    return db.query(ServicioVehiculo).offset(skip).limit(limit).all()

def get_servicio_vehiculo(db: Session, servicio_id: int):
    '''Obtener un servicio de vehículo por ID'''
    return db.query(ServicioVehiculo).filter(ServicioVehiculo.Id == servicio_id).first()

def get_servicios_by_vehiculo(db: Session, vehiculo_id: int):
    '''Obtener servicios por vehículo'''
    return db.query(ServicioVehiculo).filter(ServicioVehiculo.vehiculo_Id == vehiculo_id).all()

def get_servicios_by_lavador(db: Session, lavador_id: int):
    '''Obtener servicios por lavador'''
    return db.query(ServicioVehiculo).filter(ServicioVehiculo.lavador_Id == lavador_id).all()

def get_servicios_by_cajero(db: Session, cajero_id: int):
    '''Obtener servicios por cajero'''
    return db.query(ServicioVehiculo).filter(ServicioVehiculo.cajero_Id == cajero_id).all()

def get_servicios_by_fecha(db: Session, fecha: date):
    '''Obtener servicios por fecha'''
    return db.query(ServicioVehiculo).filter(ServicioVehiculo.fecha == fecha).all()

def create_servicio_vehiculo(db: Session, servicio: schema_usuario_vehiculo_servicio.UsuarioVehiculoServicioCreate):
    '''Crear un nuevo servicio de vehículo'''
    db_servicio = ServicioVehiculo(**servicio.model_dump())
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio_vehiculo(db: Session, servicio_id: int, servicio: schema_usuario_vehiculo_servicio.UsuarioVehiculoServicioUpdate):
    '''Actualizar un servicio de vehículo existente'''
    db_servicio = get_servicio_vehiculo(db, servicio_id)
    if db_servicio:
        update_data = servicio.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_servicio, key, value)
        db.commit()
        db.refresh(db_servicio)
    return db_servicio

def delete_servicio_vehiculo(db: Session, servicio_id: int):
    '''Eliminar un servicio de vehículo por ID'''
    db_servicio = get_servicio_vehiculo(db, servicio_id)
    if db_servicio:
        db.delete(db_servicio)
        db.commit()
    return db_servicio