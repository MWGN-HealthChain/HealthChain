from sqlalchemy import Column, String, DateTime, Boolean, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .base import Base, gen_uuid


class Hospital(Base):
    __tablename__ = "providers"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    facility_name = Column(String(255), nullable=False)
    license_number = Column(String(255), unique=True, nullable=False)
    address = Column(Text, nullable=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    credentials = relationship("HealthCredential", back_populates="provider")

    def __repr__(self):
        return f"<Provider {self.facility_name}>"
