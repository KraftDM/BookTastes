from sqlalchemy import (
    Column,
    Integer,
    String,
)

from .meta import Base


class Product(Base):
    """
    Класс продукта(питания).
    Введен для возможности создания справочника продуктов для упрощенного создания рецептов
    """
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

