from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base


class User(Base):
    """
    Данный класс является хранителем полной информации о пользователе
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
