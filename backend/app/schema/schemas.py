from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime


# ---------- PATIENT ----------
class PatientCreateDTO(BaseModel):
    first_name: str
    last_name: str
    phone_number: Optional[constr(min_length=10, max_length=15)]
    email: Optional[EmailStr]
    date_of_birth: Optional[str]


class PatientLoginDTO(BaseModel):
    first_name: str
    last_name: str
    patient_id: str


class PatientResponseDTO(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: Optional[EmailStr]
    phone_number: Optional[str]
    date_of_birth: Optional[str]
    is_active: bool
    created_at: datetime


# ---------- HOSPITAL ----------
class HospitalCreateDTO(BaseModel):
    facility_name: str
    license_number: str
    address: Optional[str]


class HospitalLoginDTO(BaseModel):
    license_number: str


class HospitalResponseDTO(BaseModel):
    id: str
    facility_name: str
    license_number: str
    address: Optional[str]
    is_verified: bool
    created_at: datetime


# ---------- MEDICAL RECORD ----------
class MedicalRecordCreateDTO(BaseModel):
    provider_id: str
    patient_id: str
    doctor_name: str
    record_type: str
    record_date: str
    symptoms: Optional[str]
    prescription: Optional[str]
    vital_sign: Optional[str]
    additional_note: Optional[str]
    title: str
    description: Optional[str]


class MedicalRecordResponseDTO(BaseModel):
    id: str
    provider_id: str
    patient_id: str
    doctor_name: str
    record_type: str
    record_date: str
    symptoms: Optional[str]
    prescription: Optional[str]
    vital_sign: Optional[str]
    additional_note: Optional[str]
    title: str
    description: Optional[str]
    walrus_blob_id: Optional[str]
    sui_object_id: Optional[str]
    status: str
    issued_at: datetime
    expires_at: Optional[datetime]
    revoked_at: Optional[datetime]
