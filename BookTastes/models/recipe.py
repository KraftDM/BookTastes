from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    DateTime,
    Index
)
from sqlalchemy.orm import relationship

from .meta import Base


class Recipe(Base):
    """
    """
    __tablename__ = 'recipe'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    time = Column(Integer, nullable=False)
    complexity = Column(Integer, nullable=False, default=0)
    count_of_portion = Column(Integer, nullable=False, default=1)
    creation_date = Column(DateTime, nullable=False)
    recipe_products = relationship("RecipeProduct")
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship("User")

    comments = relationship("Comment")
    ratings = relationship("Rating")

    Index('idx_recipe_user_id', author_id)
