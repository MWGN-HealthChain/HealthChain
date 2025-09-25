from ..model import Patient
from ..db import SessionLocal


class PatientRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, patient: Patient):
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def get_by_id(self, patient_id):
        return self.db.query(Patient).filter(Patient.id == patient_id).one_or_none()

    def get_by_name_and_id(self, first_name, last_name, patient_id):
        return (
            self.db.query(Patient)
            .filter(
                Patient.first_name == first_name,
                Patient.last_name == last_name,
                Patient.id == patient_id,
            )
            .one_or_none()
        )
