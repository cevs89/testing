import sqlalchemy as field
from sqlalchemy.sql import func


class BaseModels:
    """
    Modelo base para reutilizar en todos los modelos
    """

    id = field.Column(field.Integer, primary_key=True, index=True)
    is_active = field.Column(
        field.Boolean,
        default=True,
    )
    created_at = field.Column(field.DateTime(timezone=True), default=func.now())
    modified_at = field.Column(field.DateTime(timezone=True), onupdate=func.now())
