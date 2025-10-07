
from fastapi import HTTPException
from sqlalchemy.orm import Session,selectinload
from app.core.constants import INITIAL_PRODUCT_SERIAL_NUMBER
from app.models.product import Product
from app.models.product_lot import ProductLot
from app.schemas.product import ProductCreate, ProductOut
from app.core.logger import logger
from datetime import datetime

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

def create_product(db:Session, payload : ProductCreate, user_id:int):
  try:
  
    existing_product = Product.active(db.query(Product).filter(Product.name == payload.name)).first()
    if existing_product:
        raise HTTPException(status_code=409, detail="Product already exists.")

    next_serial = generate_next_serial_number(db)

    new_product = Product(
    name =payload.name,
    unit = payload.unit,
    serialNumber = next_serial,
    categoryId = payload.categoryId,
    createdBy = user_id
    )
    db.add(new_product)
    db.flush()

    new_lot = ProductLot(
      date = datetime.now(),
      supplierId = payload.supplierId,
      productId = new_product.id,
      quantity = payload.quantity,
      buyingPrice = payload.buyingPrice,
      sellingPrice = payload.sellingPrice,
      createdBy = user_id
    )
    db.add(new_lot)
    db.commit()
    logger.info(f"Product created: {payload.name}")
    return {"success": True, "message": "Product created successfully."}

  except HTTPException:
        raise
  except Exception as e:
      db.rollback()
      logger.error(f"Failed to create category: {e}")
      raise HTTPException(status_code=500, detail="Failed to create category.")


def generate_next_serial_number(db: Session) -> str:
    last_product = db.query(Product).order_by(Product.id.desc()).first()
    if last_product and last_product.serialNumber:
        try:
            last_serial = int(last_product.serialNumber)
        except ValueError:
            last_serial = INITIAL_PRODUCT_SERIAL_NUMBER
        next_serial = last_serial + 1
    else:
        next_serial = INITIAL_PRODUCT_SERIAL_NUMBER

    return f"{next_serial}"
 
