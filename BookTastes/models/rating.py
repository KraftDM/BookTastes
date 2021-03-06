from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    Index
)
from sqlalchemy.orm import relationship

from .meta import Base


class Rating(Base):
    """
    """
    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)

    score = Column(Integer, nullable=False)

    recipe_id = Column(Integer, ForeignKey('recipe.id'), nullable=False)
    recipe = relationship("Recipe", back_populates="ratings")

    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship("User")

    creation_date = Column(DateTime, nullable=False)

    Index('idx_rating_recipe_id', recipe_id)
    Index('idx_rating_user_id', author_id)
