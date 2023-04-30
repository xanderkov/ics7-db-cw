from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, Text, Double, Date
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

    id_vis = Column(Integer, ForeignKey('visitor.id'), primary_key=True)
    id_cam = Column(Integer, ForeignKey('camera.id'), primary_key=True)


class Shelf(BASE):
    __tablename__ = 'Shelf'
    
    location = Column(Text)
    length = Column(Double)
    
    

class ShelfVisitor(BASE):
    __tablename__ = 'ShelfVisitor'
    
    id_shelf = Column(Integer, ForeignKey('shelf.id'), primary_key=True)
    id_cam = Column(Integer, ForeignKey('camera.id'), primary_key=True)
    

class Product(BASE):
    __tablename__ = 'Product'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    location = Column(Text)
    dataEnd = Column(Date)
    wieght = Column(Double)
    status = Column(Integer)
    price = Column(Integer)

class ShelfProduct(BASE):
    __tablename__ = 'ShelfProduct'
    
    id_shelf = Column(Integer, ForeignKey('shelf.id'), primary_key=True)
    id_product = Column(Integer, ForeignKey('product.id'), primary_key=True)



class ChainStore(BASE):
    __tablename__ = 'ChainStore'
    
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    location = Column(Text)
    nameDir = Column(Text)
    inclome = Column(Double)
    consumption = Column(Double)
