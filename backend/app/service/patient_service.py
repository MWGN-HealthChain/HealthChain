from ..repository import PatientRepository
from ..model import Patient


class PatientService:
    def __init__(self):
        self.repo = PatientRepository()

    def create_patient(self, first_name, last_name, email=None, phone_number=None, date_of_birth=None):
        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth
        )
        return self.repo.create(patient)

    def login_patient(self, first_name, last_name, patient_id):
        return self.repo.find_by_credentials(first_name, last_name, patient_id)
