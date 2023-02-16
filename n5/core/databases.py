import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from n5.core.config import settings

logger = logging.getLogger(__name__)

if not settings.DATABASE_URL:
    raise ValueError("'DATABASE_URL ' is None!")

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
