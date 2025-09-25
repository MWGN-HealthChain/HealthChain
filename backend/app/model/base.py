import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def gen_uuid():
    """Generate a UUID string for primary keys."""
    return str(uuid.uuid4())
