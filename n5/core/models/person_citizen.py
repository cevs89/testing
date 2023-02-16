import sqlalchemy as field
from sqlalchemy.orm import validates

from n5.core.databases import Base
from n5.core.models.base import BaseModels


class PersonCitizen(BaseModels, Base):
    __tablename__ = "person_citizen"
    person_name = field.Column(field.String(), nullable=False)
    person_email = field.Column(field.String(), nullable=False)

    @validates("person_email")
    def validate_email(self, key, value):
        if "@" not in value:
            raise ValueError("failed email validation")
        return value

    def __repr__(self):
        return f"Person: ({self.person_name})"

    def __str__(self):
        return self.person_name
