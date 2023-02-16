from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import n5.admin.views.person_citizen as persons
from n5.core.config import settings
from n5.core.databases import Base, engine

Base.metadata.create_all(bind=engine)
# inint FastAPI
app = FastAPI(title=settings.app_name)

"""
include every routers
"""
app.include_router(persons.router)

app.mount("/static", StaticFiles(directory="n5/admin/static/"), name="static")
