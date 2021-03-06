from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Table,
    Index
)
from sqlalchemy.orm import relationship

from .meta import Base

association_table_recipe_cook_2_recipe = Table('recipe_book_2_recipe', Base.metadata,
                                               Column('recipe_book_id', Integer, ForeignKey('recipe_book.id')),
                                               Column('recipe_id', Integer, ForeignKey('recipe.id'))
                                               )


class RecipeBook(Base):
    """
    """
    __tablename__ = 'recipe_book'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    recipes = relationship("Recipe", secondary=association_table_recipe_cook_2_recipe)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship("User")

    Index('idx_recipe_book_user_id', author_id)
