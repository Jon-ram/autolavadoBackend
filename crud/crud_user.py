from sqlalchemy.orm import Session
from models.modelUser import User
from schemas.schema_user import UserCreate, UserUpdate, UserLogin
import bcrypt

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    '''Obtener todos los usuarios'''
    return db.query(User).offset(skip).limit(limit).all()

def get_usuario(db: Session, user_id: int):
    '''Obtener un usuario por ID'''
    return db.query(User).filter(User.Id == user_id).first()

def get_usuario_by_email(db: Session, email: str):
    '''Obtener usuario por email'''
    return db.query(User).filter(User.correo_electronico == email).first()

def get_usuario_by_telefono(db: Session, telefono: str):
    '''Obtener usuario por teléfono'''
    return db.query(User).filter(User.numero_telefono == telefono).first()

def hash_password(password: str) -> str:
    '''Hashea una contraseña usando bcrypt, manejando el límite de 72 bytes'''
    # Convertir a bytes y truncar si es necesario
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    
    # Generar salt y hashear
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''Verifica una contraseña contra su hash'''
    try:
        # Truncar la contraseña plana de la misma manera
        password_bytes = plain_password.encode('utf-8')
        if len(password_bytes) > 72:
            password_bytes = password_bytes[:72]
        
        # Verificar
        return bcrypt.checkpw(password_bytes, hashed_password.encode('utf-8'))
    except Exception:
        return False

def create_usuario(db: Session, usuario: UserCreate):
    '''Crear un nuevo usuario'''
    # Verificar si el email ya existe
    db_usuario = get_usuario_by_email(db, email=usuario.correo_electronico)
    if db_usuario:
        return None
    
    # Verificar si el teléfono ya existe
    db_usuario = get_usuario_by_telefono(db, telefono=usuario.numero_telefono)
    if db_usuario:
        return None
    
    # Hashear la contraseña
    hashed_password = hash_password(usuario.contrasena)
    
    db_usuario = User(
        rol_Id=usuario.rol_Id,
        nombre=usuario.nombre,
        papellido=usuario.papellido,
        sapellido=usuario.sapellido,
        direccion=usuario.direccion,
        correo_electronico=usuario.correo_electronico,
        numero_telefono=usuario.numero_telefono,
        contrasena=hashed_password,
        estatus=usuario.estatus
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, user_id: int, usuario: UserUpdate):
    '''Actualizar un usuario existente'''
    db_usuario = get_usuario(db, user_id)
    if db_usuario:
        update_data = usuario.model_dump(exclude_unset=True)
        if 'contrasena' in update_data:
            update_data['contrasena'] = hash_password(update_data['contrasena'])
        
        for key, value in update_data.items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, user_id: int):
    '''Eliminar un usuario por ID'''
    db_usuario = get_usuario(db, user_id)
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

def authenticate_user(db: Session, login_data: UserLogin):
    '''Autenticar usuario'''
    user = None
    if login_data.correo_electronico:
        user = get_usuario_by_email(db, login_data.correo_electronico)
    elif login_data.numero_telefono:
        user = get_usuario_by_telefono(db, login_data.numero_telefono)
    
    if user and verify_password(login_data.contrasena, user.contrasena):
        return user
    return None