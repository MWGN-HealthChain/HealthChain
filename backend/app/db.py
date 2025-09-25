from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Import the shared Base and all models
from .model import Base  # this will also import User, Provider, HealthCredential

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False))


def init_db(app):
    """
    Initialize the database connection and attach session to the Flask app.
    """
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], future=True)
    SessionLocal.configure(bind=engine)

    # Create all tables (based on imported models)
    Base.metadata.create_all(bind=engine)

    # Attach session factory to the app for easy access
    app.session = SessionLocal
