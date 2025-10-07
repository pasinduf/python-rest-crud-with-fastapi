from fastapi import APIRouter
from fastapi.params import Depends
from app.schemas.common import CreateResponse
from app.schemas.product import ProductCreate, ProductOut
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.crud import product

router = APIRouter()

@router.get("/products/", response_model = list[ProductOut])
def get_products(db:Session = Depends(get_db)):
    return product.get_active_products(db)

@router.get("/products/all", response_model = list[ProductOut])
def get_all_products(db:Session = Depends(get_db)):
    return product.get_all_products(db)

@router.post("/products/",response_model=CreateResponse)
def create_product(payload:ProductCreate, db:Session = Depends(get_db)):
    user_id=1
    return product.create_product(db, payload, user_id)