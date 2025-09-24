from sqlalchemy import Column, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from .db import Base

def gen_uuid():
    return str(uuid.uuid4())

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    first_name = Column(String(120))
    last_name = Column(String(120))
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(30))
    date_of_birth = Column(DateTime)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Provider(Base):
    __tablename__ = "providers"
    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    facility_name = Column(String(255))
    license_number = Column(String(255))
    address = Column(Text)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class HealthCredential(Base):
    __tablename__ = "health_credentials"
    id = Column(UUID(as_uuid=False), primary_key=True, default=gen_uuid)
    provider_id = Column(UUID(as_uuid=False), ForeignKey("providers.id"))
    patient_id = Column(UUID(as_uuid=False), ForeignKey("users.id"))
    title = Column(String(255))
    description = Column(Text)
    document_hash = Column(String(255))   # hash of file for integrity
    walrus_blob_id = Column(String(255))  # walrus reference
    sui_object_id = Column(String(255))   # reference on Sui
    status = Column(String(50), default="issued")  # issued, revoked
    issued_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=True)
    revoked_at = Column(DateTime(timezone=True), nullable=True)
