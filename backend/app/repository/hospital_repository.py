from ..model import Hospital
from ..db import SessionLocal


class HospitalRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create(self, hospital: Hospital):
        self.db.add(hospital)
        self.db.commit()
        self.db.refresh(hospital)
        return hospital

    def get_by_license(self, license_number):
        return (
            self.db.query(Hospital)
            .filter(Hospital.license_number == license_number)
            .one_or_none()
        )
