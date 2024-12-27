from fastapi import FastAPI
from routes import products  # Importer les routes des produits
from auth import router as auth_router  # Importer les routes d'authentification
from models import SQLModel, ProductCategory, Product, ProductModel
from config import engine

# Initialiser l'application FastAPI
app = FastAPI(
    title="AdventureWorks API",
    description="API CRUD pour gérer les produits AdventureWorks avec authentification JWT",
    version="1.0.0",
)

# Création des tables si elles n'existent pas encore
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Inclure les routes des produits
app.include_router(products.router, prefix="/api/v1", tags=["Products"])

# Inclure les routes d'authentification
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
