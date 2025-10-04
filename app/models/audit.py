from sqlalchemy import Column, Integer, DateTime, func
from datetime import datetime

class AuditMixin:
    createdBy = Column(Integer, nullable=True)  # createdBy
    createdAt = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updatedAt = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=True)
    deletedAt = Column(DateTime(timezone=True), nullable=True)  # soft delete

    @classmethod
    def active(cls, query):
        return query.filter(cls.deletedAt == None)
    
    def soft_delete(self):
        self.deletedAt = datetime.now()
