from sqlalchemy import (
    Column, String, DateTime, Boolean, Text, ForeignKey
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from .db import Base


def gen_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_number = Column(String(30), unique=True, nullable=True)
    date_of_birth = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    credentials = relationship("HealthCredential", back_populates="patient")

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"


class Provider(Base):
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


class HealthCredential(Base):
    __tablename__ = "health_credentials"

    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    provider_id = Column(UUID(as_uuid=False), ForeignKey("providers.id"), nullable=False)
    patient_id = Column(UUID(as_uuid=False), ForeignKey("users.id"), nullable=False)

    title = Column(String(255), nullable=False)   # e.g. "Blood Test Result"
    description = Column(Text, nullable=True)

    document_hash = Column(String(255), nullable=True)   # file integrity hash
    walrus_blob_id = Column(String(255), nullable=True)  # Walrus reference
    sui_object_id = Column(String(255), nullable=True)   # On-chain ref (Sui)

    status = Column(String(50), default="issued")  # issued, revoked
    issued_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    revoked_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    provider = relationship("Provider", back_populates="credentials")
    patient = relationship("User", back_populates="credentials")

    def __repr__(self):
        return f"<HealthCredential {self.title} for patient {self.patient_id}>"
