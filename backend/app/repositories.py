from .models import HealthCredential, User, Provider
from .db import SessionLocal
from sqlalchemy.exc import NoResultFound

class CredentialRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, credential: HealthCredential):
        self.db.add(credential)
        self.db.commit()
        self.db.refresh(credential)
        return credential

    def get_by_id(self, id):
        return self.db.query(HealthCredential).filter(HealthCredential.id==id).one_or_none()

    def update(self, credential):
        self.db.add(credential)
        self.db.commit()
        self.db.refresh(credential)
        return credential

    def list_by_patient(self, patient_id):
        return self.db.query(HealthCredential).filter(HealthCredential.patient_id==patient_id).all()
