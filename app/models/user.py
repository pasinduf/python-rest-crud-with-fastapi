
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from app.models.audit import AuditMixin


class User(Base, AuditMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    password = Column(String, nullable=False)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)  
