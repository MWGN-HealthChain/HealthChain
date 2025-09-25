from ..model import MedicalRecord
from ..db import SessionLocal


class MedicalRecordRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, record: MedicalRecord):
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def get_by_id(self, record_id):
        return (
            self.db.query(MedicalRecord)
            .filter(MedicalRecord.id == record_id)
            .one_or_none()
        )

    def update(self, record: MedicalRecord):
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

    def list_by_patient(self, patient_id):
        return (
            self.db.query(MedicalRecord)
            .filter(MedicalRecord.patient_id == patient_id)
            .all()
        )
