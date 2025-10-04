
from sqlalchemy.orm import Session,selectinload
from app.models.product import Product
from app.schemas.product import ProductOut

def get_all_products(db:Session):
 products =  db.query(Product).options(selectinload(Product.lots),selectinload(Product.category)).all()
 result = [
  ProductOut(
    id=p.id,
    name=p.name,
    unit=p.unit,
    serialNumber=p.serialNumber,
    category=p.category.name,
    lots=p.lots
  )
  for p in products
 ]
 return result

def get_active_products(db:Session):
 products=  Product.active(db.query(Product).options(selectinload(Product.lots),selectinload(Product.category))).all()
 result = [
  ProductOut(
    id=p.id,
    name=p.name,
    unit=p.unit,
    serialNumber=p.serialNumber,
    category=p.category.name,
    lots=p.lots
  )
  for p in products
 ]
 return result