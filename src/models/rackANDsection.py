from sqlalchemy import Column, Integer , String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


# RACK
class Rack(Base):
    __tablename__="racks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    racksection = relationship ("RackSection" , back_populates="rack")


# SECTION
class Section(Base):
    __tablename__="section"
    id = Column(Integer, primary_key=True ,index=True)
    name = Column(String, nullable=False)

    racksection = relationship ("RackSection" , back_populates="section")


# RACK AND SECTION CONNECTION
class RackSection(Base):
    __tablename__="racksection"
    id = Column(Integer,primary_key=True , index=True)
    rack_id = Column(Integer,ForeignKey("rack.id"))
    section_id = Column(Integer,ForeignKey("section.id"))

    rack = relationship ("Rack",back_populates="racksection")
    section = relationship ("Section", back_populates="racksection")

    product_section = relationship ("ProductSection", back_populates="racksection")
    purchase = relationship ("Purchase", back_populates="racksection")