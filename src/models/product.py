from sqlalchemy import Column, Integer , String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.config.database import Base


#  BRAND
class Brand(Base):
    __tablename__="brand"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    product = relationship ("Product", back_populates="brand")


#CATEGORY
class Category(Base):
    __tablename__="category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    product = relationship ("Product" , back_populates="category")


#PRODUCT
class Product(Base):
    __tablename__="product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category_id = Column(Integer,ForeignKey("category.id"))
    brand_id = Column(Integer,ForeignKey("brand.id"))
    price = Column(Float,nullable=False)

    category = relationship ("Category", back_populates="product")
    brand = relationship ("Brand", back_populates="product")
    product_section = relationship ("ProductSection", back_populates="product",cascade="all, delete-orphan")
    purchase = relationship ("Purchase", back_populates="product",cascade="all, delete-orphan")


#PRODUCT AND RACK SECTION
class ProductSection(Base):
    __tablename__="product_section"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    racksection_id = Column(Integer, ForeignKey("racksection.id"))
    quantity = Column(Integer,nullable=False)

    product = relationship ("Product", back_populates="product_section")
    racksection = relationship ("RackSection", back_populates="product_section")