import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from n5.core.config import settings

logger = logging.getLogger(__name__)

if not settings.DATABASE_URL:
    raise ValueError("'DATABASE_URL ' is None!")

engine = create_engine(
    settings.DATABASE_URL,
    pool_recycle=3600,
    connect_args={"connect_timeout": 20, "check_same_thread": False},
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class MySuperContextManager:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


async def get_db():
    with MySuperContextManager() as db:
        yield db
