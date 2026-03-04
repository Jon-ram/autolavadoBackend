from fastapi import FastAPI
from routes.routes_user import usuario_router
from routes.routes_rols import rol_router
from routes.routes_servicio import servicio_router
from routes.routes_vehiculos import vehiculo_router
from routes.routes_usuario_vehiculo_servicio import servicio_vehiculo_router

# Importar los modelos para que SQLAlchemy los conozca
from models.modelUser import User
from models.modelRols import Rols
from models.modelServicio import Servicio
from models.modelVehiculos import Vehiculo
from models.model_usuario_vehiculo_servicio import ServicioVehiculo
from config.db import engine, Base

# Crear todas las tablas
print("🔄 Creando tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas/verificadas")

app = FastAPI(
    title="API de Autolavado",
    description="API para gestión de autolavado con autenticación JWT",
    version="1.0.0"
)

# Incluir todos los routers
app.include_router(usuario_router)
app.include_router(rol_router)
app.include_router(servicio_router)
app.include_router(vehiculo_router)
app.include_router(servicio_vehiculo_router)

@app.get("/")
async def root():
    return {
        "message": "API de Autolavado",
        "documentation": "/docs",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}