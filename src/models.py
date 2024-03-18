import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(String(250))
    weight = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    img_url = Column(String(250))

    def to_dict(self):
        return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    rotation_period = Column(String(250))
    orbital_period = Column(String(250))
    surface_water = Column(String(250))
    img_url = Column(String(250))

    def to_dict(self):
        return {}

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey(Character.id))
    planet_id = Column(Integer, ForeignKey(Planets.id))
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    #establish relation
    user = relationship('User', foreign_keys='Favorites.user_id')
    char = relationship('Character', foreign_keys='Favorites.char_id')
    planet = relationship('Planets', foreign_keys='Favorites.planet_id')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
