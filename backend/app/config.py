import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/healthpass")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WALRUS_API_URL = os.getenv("WALRUS_API_URL", "https://walrus.api/")  # replace with real endpoint
    SUI_RPC_URL = os.getenv("SUI_RPC_URL", "https://sui-rpc.example/")  # replace with real endpoint
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
