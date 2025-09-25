from .repositories import CredentialRepository
from .models import HealthCredential
from .exceptions import NotFoundError, BadRequestError
from .walrus_client import walrus_upload
from .sui_client import sui_register_credential

class CredentialService:
    def __init__(self):
        self.repo = CredentialRepository()

    def issue_credential(self, provider_id, patient_id, title, description, file_bytes, filename):
        # 1. Upload file to Walrus -> gets walrus_blob_id + hash/url
        walrus_res = walrus_upload(file_bytes, filename)
        if not walrus_res:
            raise BadRequestError("Failed to upload file to Walrus")

        document_hash = walrus_res.get("hash")
        walrus_blob_id = walrus_res.get("blob_id")
        # 2. Create DB record (sui_object_id will be set after on-chain)
        credential = HealthCredential(
            provider_id=provider_id,
            patient_id=patient_id,
            title=title,
            description=description,
            document_hash=document_hash,
            walrus_blob_id=walrus_blob_id,
            status="issued"
        )
        credential = self.repo.create(credential)
        # 3. Register on Sui (store object or call Move module)
        sui_res = sui_register_credential(credential)
        # sample response: {"object_id": "...", "tx_hash": "..."}
        if sui_res:
            credential.sui_object_id = sui_res.get("object_id")
            self.repo.update(credential)
        return credential

    def get_credential(self, credential_id):
        cred = self.repo.get_by_id(credential_id)
        if not cred:
            raise NotFoundError("Credential not found")
        return cred
