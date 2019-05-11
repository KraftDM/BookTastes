from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Table
)
from sqlalchemy.orm import relationship

from .meta import Base

association_table = Table('recipe_book_2_recipe', Base.metadata,
                          Column('recipe_book_id', Integer, ForeignKey('recipe_book.id')),
                          Column('recipe_id', Integer, ForeignKey('recipe.id'))
                          )


class RecipeBook(Base):
    """
    Класс описывающий сборник рецептов
    """
    __tablename__ = 'recipe_book'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    recipes = relationship("Recipe", secondary=association_table)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship("User")

