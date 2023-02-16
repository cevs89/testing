from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

from n5.core.databases import Base, engine, get_db

# from n5.core.models import PersonCitizen
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", status_code=status.HTTP_201_CREATED)
async def create_environment(db: Session = Depends(get_db)):

    return {"details": "Success"}
