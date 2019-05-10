from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base


class UnitType(Base):
    """
    Единицы измерения(кг, г, шт...)
    """
    __tablename__ = 'unit_type'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

