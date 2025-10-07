from fastapi import FastAPI
from app.api import product as product_router
from app.api import category as category_router
from app.api import auth as auth_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router.router, prefix="/api", tags=["products"])
app.include_router(category_router.router, prefix="/api", tags=["categories"])
app.include_router(auth_router.router, prefix="/api", tags=["auth"])
