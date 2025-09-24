"""
Sui client placeholder.

Typical pattern:
  - Use a Sui SDK or RPC to submit a transaction that creates a credential object
  - The transaction returns an object id or transaction hash
  - Save that object id to your DB record

You will likely use a Sui HTTP RPC or official SDK in JS/Python. A common design:
  - Backend creates a transaction payload containing credential metadata and walrus_blob_id
  - Backend signs the transaction (or uses a server controlled key) and submits it
  - You can store either the returned object_id or tx_hash for verification later
"""

from flask import current_app

def sui_register_credential(credential):
    # PSEUDO: implement using Sui SDK or call Move module
    # Example return shape:
    # {"object_id": "0xabc...", "tx_hash": "0x123..."}
    current_app.logger.info("Would call Sui to register credential %s", credential.id)
    # For now, return a fake object id until you implement real call
    return {"object_id": f"fake_sui_object_{credential.id}"}
