from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .base import Base, gen_uuid


class MedicalRecord(Base):
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
