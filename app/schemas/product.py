from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_serializer

class ProductBase(BaseModel):
    id: int

class ProductLotOut(BaseModel):
    id: int
    date: datetime
    quantity : float
    buyingPrice : float
    sellingPrice : float
    
    @field_serializer("date")
    def serialize_date(self, value: datetime) -> str:
        return value.strftime("%Y-%m-%d")

    model_config = ConfigDict(from_attributes=True)


class ProductOut(ProductBase):
    name:str
    serialNumber:str
    unit:str
    category:str
    lots:list[ProductLotOut] = []

    model_config = ConfigDict(from_attributes=True)
