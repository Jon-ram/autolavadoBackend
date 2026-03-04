from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
import config.db
from crud import crud_productos
from schemas import schema_productos
from config.security import get_current_user

producto_router = APIRouter(prefix="/productos", tags=["Productos"])

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints protegidos (requieren token)
@producto_router.get("/", response_model=List[schema_productos.Producto])
async def read_productos(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener todos los productos'''
    productos = crud_productos.get_productos(db=db, skip=skip, limit=limit)
    return productos

@producto_router.get("/{producto_id}", response_model=schema_productos.Producto)
async def read_producto(
    producto_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Obtener un producto por ID'''
    db_producto = crud_productos.get_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@producto_router.post("/", response_model=schema_productos.Producto, status_code=status.HTTP_201_CREATED)
async def create_producto(
    producto: schema_productos.ProductoCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Crear un nuevo producto'''
    # Verificar si ya existe un producto con el mismo nombre
    db_producto = crud_productos.get_producto_by_nombre(db, nombre=producto.nombre)
    if db_producto:
        raise HTTPException(status_code=400, detail="Producto con ese nombre ya existe")
    
    return crud_productos.create_producto(db=db, producto=producto)

@producto_router.put("/{producto_id}", response_model=schema_productos.Producto)
async def update_producto(
    producto_id: int, 
    producto: schema_productos.ProductoUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Actualizar un producto existente'''
    db_producto = crud_productos.update_producto(db=db, producto_id=producto_id, producto=producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

@producto_router.delete("/{producto_id}")
async def delete_producto(
    producto_id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    '''Eliminar un producto por ID'''
    db_producto = crud_productos.delete_producto(db=db, producto_id=producto_id)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"message": "Producto eliminado exitosamente"}