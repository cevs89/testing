from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from n5.admin.forms import CreatePersonForm
from n5.core.databases import get_db

router = APIRouter(
    prefix="/person",
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="n5/admin/templates")


@router.get("/create/", tags=["Person"])
def create_person(request: Request):
    return templates.TemplateResponse(
        "person_citizen/create.html",
        {
            "request": request,
        },
    )


@router.post("/create/")
async def create_person_save(request: Request, db: Session = Depends(get_db)):
    form = CreatePersonForm(request)
    await form.load_data()
    print(await form.load_data())
    return templates.TemplateResponse(
        "person_citizen/create.html", {"request": request, "msg": "BIEN"}
    )


@router.get("/lists/", tags=["Person"])
def lists_person(request: Request):
    return templates.TemplateResponse(
        "person_citizen/list.html",
        {
            "request": request,
        },
    )
