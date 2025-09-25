from ..repository import HospitalRepository
from ..model import Hospital


class HospitalService:
    def __init__(self):
        self.repo = HospitalRepository()

    def register_hospital(self, facility_name, license_number, address=None):
        hospital = Hospital(
            facility_name=facility_name,
            license_number=license_number,
            address=address,
            is_verified=False
        )
        return self.repo.create(hospital)

    def login_hospital(self, license_number):
        return self.repo.get_by_license(license_number)
