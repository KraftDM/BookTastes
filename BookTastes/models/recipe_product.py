from sqlalchemy import (
    Column,
    Integer,
    DECIMAL,
    ForeignKey,
    Index
)
from sqlalchemy.orm import relationship

from .meta import Base


class RecipeProduct(Base):
    """
    """
    __tablename__ = 'recipe_product'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    product = relationship("Product")
    unit_type_id = Column(Integer, ForeignKey('unit_type.id'), nullable=False)
    unit_type = relationship("UnitType")
    amount = Column(DECIMAL, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))

    Index('idx_recipe_product_unit_type_id', unit_type_id)
    Index('idx_recipe_product_recipe_id', recipe_id)
