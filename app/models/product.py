from sqlalchemy import Column, ForeignKey, Integer, String,Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.audit import AuditMixin

class Product(Base,AuditMixin):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=True)
    serialNumber = Column(String, nullable=False, unique=True)

    #many to one
    categoryId = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="products")

    #one to many
    lots = relationship("ProductLot", back_populates="product" , lazy="noload")