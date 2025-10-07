from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer,Numeric,DateTime
from app.models.audit import AuditMixin

class ProductLot(Base,AuditMixin):
    __tablename__ = "product_lots"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=True)

    #many to one   
    productId = Column(Integer, ForeignKey("products.id"), nullable=False)
    product = relationship("Product", back_populates ="lots")

    quantity = Column(Numeric(precision=10, scale=2))
    buyingPrice = Column(Numeric(precision=10, scale=2))
    sellingPrice = Column(Numeric(precision=10, scale=2))

    #many to one
    supplierId = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    supplier = relationship("Supplier", back_populates ="lots")
