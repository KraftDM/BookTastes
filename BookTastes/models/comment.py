from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime
)
from sqlalchemy.orm import relationship

from .meta import Base


class Comment(Base):
    """
    Класс, описывающий комментарий пользователем рецепта
    """
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)

    description = Column(String, nullable=False)

    recipe_id = Column(Integer, ForeignKey('recipe.id'), nullable=False)
    recipe = relationship("Recipe", back_populates="comments")

    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship("User")

    creation_date = Column(DateTime, nullable=False)
