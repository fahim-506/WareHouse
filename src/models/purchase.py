from sqlalchemy import Column, Integer , String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config.database import Base


#SALE PERSON
class Sale_Person(Base):
    __tablename__="sale_person"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact = Column(String(10) ,nullable=False)

    purchase = relationship ("Purchase", back_populates="sale_person",cascade="all, delete-orphan")


#PURCHASE
class Purchase(Base):
    __tablename__="purchase"
    id = Column(Integer, primary_key=True, index=True)
    sale_person_id = Column (Integer,ForeignKey("sale_person.id"))
    product_id = Column (Integer,ForeignKey("product.id"))
    racksection_id = Column (Integer,ForeignKey("racksection.id"))
    quantity = Column (Integer,nullable=False)
    date = Column (Date,nullable=False)

    sale_person = relationship("Sale_Person", back_populates="purchase")
    product = relationship ("Product", back_populates="purchase")
    racksection = relationship ("RackSection" , back_populates="purchase")