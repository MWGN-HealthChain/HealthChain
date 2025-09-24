from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime


# ---------- USER ----------
class UserCreateDTO(BaseModel):
    first_name: str
    last_name: str
    phone_number: constr(min_length=10, max_length=15)
    email: EmailStr
    date_of_birth: str
    password: constr(min_length=6)


class UserLoginDTO(BaseModel):
    email: EmailStr
    password: str


class UserResponseDTO(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime


# ---------- PROVIDER ----------
class ProviderCreateDTO(BaseModel):
    facility_name: str
    facility_type: str
    license_number: str
    address: str
    email: EmailStr


class ProviderResponseDTO(BaseModel):
    id: str
    facility_name: str
    facility_type: str
    license_number: str
    is_verified: bool
    created_at: datetime
    updated_at: Optional[datetime]


# ---------- CREDENTIAL ----------
class CredentialIssueDTO(BaseModel):
    provider_id: str
    patient_id: str
    credential_type: str
    title: str
    description: str
    document_hash: str


class CredentialResponseDTO(BaseModel):
    id: str
    provider_id: str
    patient_id: str
    credential_type: str
    title: str
    description: str
    sui_object_id: str
    status: str
    issued_at: datetime
    expires_at: Optional[datetime]
    revoked_at: Optional[datetime]


# ---------- VERIFICATION ----------
class VerificationRequestDTO(BaseModel):
    verifier_id: str
    credential_id: str


class VerificationResponseDTO(BaseModel):
    id: str
    verifier_id: str
    credential_id: str
    verification_hash: str
    result: str
    verified_at: datetime
