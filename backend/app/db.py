from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

Base = declarative_base()
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False))

def init_db(app):
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], future=True)
    SessionLocal.configure(bind=engine)
    Base.metadata.create_all(bind=engine)
    # attach to app for convenience
    app.session = SessionLocal
