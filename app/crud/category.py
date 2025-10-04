
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.api import category
from app.models.category import Category
from app.schemas.category import CategoryCreate
from app.core.logger import logger

def get_all_categories(db:Session):
    return db.query(Category).order_by(Category.id.asc()).all()

def get_active_categories(db:Session):
    return Category.active(db.query(Category).order_by(Category.createdAt.asc())).all()

def create_category(db:Session, payload:CategoryCreate, user_id:int):
    try:
        existing_category = Category.active(db.query(Category).filter(Category.name == payload.name)).first()
        if existing_category:
            raise HTTPException(status_code=409, detail="Category already exists.")

        category = Category(**payload.model_dump(), createdBy = user_id)
        logger.info(f"Category created: {category.name}")
        db.add(category)
        db.commit()

        return {"success": True, "message": "Category created successfully."}
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to create category: {e}")
        raise HTTPException(status_code=500, detail="Failed to create category.")
    
def update_category(db:Session, category_id:int, payload: CategoryCreate, user_id:int):
    try:
        category = Category.active(db.query(Category).filter(Category.id == category_id)).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        for key, value in payload.model_dump().items():
            setattr(category, key, value)
        category.updatedBy = user_id
        db.commit()
        logger.info(f"Category updated: {category.name}")
        return {"success": True, "message": "Category updated successfully."}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to update category: {e}")
        raise HTTPException(status_code=500, detail="Failed to update category.")

def delete_category(db:Session, category_id:int, user_id:int):
    try:
        category = Category.active(db.query(Category).filter(Category.id == category_id)).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        category.deletedBy = user_id
        category.soft_delete()
        db.commit()
        logger.info(f"Category deleted: {category.name}")
        return {"success": True, "message": "Category deleted successfully."}
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to delete category: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete category.")





