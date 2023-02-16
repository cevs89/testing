import sqlalchemy as field

from n5.core.databases import Base
from n5.core.models.base import BaseModels


class PersonOfficer(BaseModels, Base):
    __tablename__ = "person_officer"
    officer_name = field.Column(field.String(255), nullable=False)
    identification = field.Column(field.Integer, nullable=False, unique=True)

    def __repr__(self):
        return f"Officer: ({self.officer_name})"

    def __str__(self):
        return self.officer_name
