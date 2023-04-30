from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from sqlalchemy.types import Float
from sqlalchemy import PrimaryKeyConstraint

BASE = declarative_base()


class Visitor(BASE):
    __tablename__ = 'Visitor'
    
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    location = Column(Text)
    view = Column(Text)
    detection = Column(Text)


class Camera(BASE):
    __tablename__ = 'Camera'
    
    id = Column(Integer, primary_key=True)
    location = Column(Text)
    resolution = Column(Text)
    rotation = Column(Text)
    cam_type = Column(Text)


class CameraVisiotor(BASE):
    __tablename__ = 'CameraVisiotor'

    id_vis = Column(Integer, ForeignKey('Visitor.id'), primary_key=True)
    id_cam = Column(Integer, ForeignKey('Camera.id'), primary_key=True)


class Shelf(BASE):
    __tablename__ = 'Shelf'
    
    id = Column(Integer, primary_key=True)
    location = Column(Text)
    length = Column(Float)
    
    

class ShelfVisitor(BASE):
    __tablename__ = 'ShelfVisitor'
    
    id_shelf = Column(Integer, ForeignKey('Shelf.id'), primary_key=True)
    id_cam = Column(Integer, ForeignKey('Camera.id'), primary_key=True)
    

class Product(BASE):
    __tablename__ = 'Product'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    location = Column(Text)
    dataEnd = Column(Date)
    wieght = Column(Float)
    status = Column(Integer)
    price = Column(Integer)

class ShelfProduct(BASE):
    __tablename__ = 'ShelfProduct'
    
    id_shelf = Column(Integer, ForeignKey('Shelf.id'), primary_key=True)
    id_product = Column(Integer, ForeignKey('Product.id'), primary_key=True)



class ChainStore(BASE):
    __tablename__ = 'ChainStore'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    location = Column(Text)
    nameDir = Column(Text)
    inclome = Column(Float)
    consumption = Column(Float)

