from ..repository import MedicalRecordRepository
from ..model import MedicalRecord
from ..exceptions import BadRequestError, NotFoundError
from ..walrus_client import walrus_upload
from ..sui_client import sui_register_credential


class MedicalRecordService:
    def __init__(self):
        self.repo = MedicalRecordRepository()

    def add_record(self, provider_id, patient_id, record_data, file=None):
        """
        Add a medical record with optional file upload.
        - Uploads file to Walrus (if provided)
        - Stores metadata in DB
        - Registers on Sui blockchain
        """
        document_hash = None
        walrus_blob_id = None

        # If file is provided, push to Walrus
        if file:
            file_bytes, filename = file
            walrus_res = walrus_upload(file_bytes, filename)
            if not walrus_res:
                raise BadRequestError("Failed to upload file to Walrus")

            document_hash = walrus_res.get("hash")
            walrus_blob_id = walrus_res.get("blob_id")

        # Create record object
        record = MedicalRecord(
            provider_id=provider_id,
            patient_id=patient_id,
            title=record_data.get("title"),
            description=record_data.get("description"),
            doctor_name=record_data.get("doctor_name"),
            record_type=record_data.get("record_type"),
            record_date=record_data.get("record_date"),
            symptoms=record_data.get("symptoms"),
            prescription=record_data.get("prescription"),
            vital_sign=record_data.get("vital_sign"),
            additional_note=record_data.get("additional_note"),
            document_hash=document_hash,
            walrus_blob_id=walrus_blob_id,
            status="issued"
        )
        record = self.repo.create(record)

        # Register on Sui
        sui_res = sui_register_credential(record)
        if sui_res:
            record.sui_object_id = sui_res.get("object_id")
            self.repo.update(record)

        return record

    def get_record(self, record_id: str):
        record = self.repo.get_by_id(record_id)
        if not record:
            raise NotFoundError("Medical record not found")
        return record

    def list_by_patient(self, patient_id: str):
        return self.repo.list_by_patient(patient_id)
