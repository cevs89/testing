import enum

import sqlalchemy as field
from sqlalchemy.orm import relationship

from n5.core.databases import Base
from n5.core.models import PersonCitizen
from n5.core.models.base import BaseModels


class TypeVehiculeChoice(enum.Enum):
    car = "Car"
    moto = "Motorcycle"
    big_card = "Cargo truck"


class Infractions(BaseModels, Base):
    __tablename__ = "infractions"

    patent = field.Column(field.String(25), nullable=False, unique=True)
    brand = field.Column(field.String, nullable=False)
    color = field.Column(field.String, nullable=False)
    reason_infraction = field.Column(field.Text, nullable=False)
    timestamp = field.Column(field.DateTime(timezone=True))
    vehicule_type = field.Column(
        field.Enum(TypeVehiculeChoice), default=TypeVehiculeChoice.car, nullable=False
    )
    person_citizen_id = field.Column(field.Integer, field.ForeignKey(PersonCitizen.id))
    person_citizen = relationship(PersonCitizen, cascade="all, delete-orphan")

    def __str__(self):
        return self.patent
