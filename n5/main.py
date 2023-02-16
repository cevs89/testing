from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from n5.core.databases import Base, engine

# from n5.core.models import PersonCitizen
Base.metadata.create_all(bind=engine)

app = FastAPI()
from n5.core.databases import SessionLocal


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


@app.get("/", status_code=status.HTTP_201_CREATED)
async def create_environment(db: Session = Depends(get_db)):

    return {"details": "Success"}
