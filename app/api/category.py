
from fastapi import APIRouter
from fastapi.params import Depends
from app.api.auth_handler import get_current_user
from app.core.database import get_db
from app.schemas.category import CategoryOut, CategoryCreate
from sqlalchemy.orm import Session
from app.crud import category
from app.schemas.common import CreateResponse


router = APIRouter()

@router.get("/categories/",response_model=list[CategoryOut])
def get_categories(db:Session = Depends(get_db)):
    return category.get_active_categories(db)

@router.get("/categories/all",response_model=list[CategoryOut])
def get_all_categories(db:Session = Depends(get_db)):
    return category.get_all_categories(db)


@router.post("/categories/",response_model=CreateResponse)
def create_category(payload:CategoryCreate, db:Session = Depends(get_db),user = Depends(get_current_user)):
    return category.create_category(db, payload, user.id)

@router.put("/categories/{category_id}",response_model=CreateResponse)
def update_category(category_id:int, payload:CategoryCreate, db:Session = Depends(get_db),user = Depends(get_current_user)):
    return category.update_category(db, category_id,payload, user.id)


@router.delete("/categories/{category_id}",response_model=CreateResponse)
def delete_category(category_id:int, db:Session = Depends(get_db),user = Depends(get_current_user)):
    return category.delete_category(db, category_id, user.id)


