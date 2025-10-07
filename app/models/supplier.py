from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.audit import AuditMixin

class Supplier(Base,AuditMixin):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contactNumber = Column(String, nullable=True)
    address = Column(String, nullable=True)

    #one to many
    lots = relationship("ProductLot", back_populates="supplier" , lazy="noload")