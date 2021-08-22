from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(25), nullable=False)
    email_address = Column(String(50), nullable=False)

    gifs = relationship("Collection")


class Gif(Base):
    __tablename__ = "gifs"

    gif_id = Column(Integer, primary_key=True, index=True)
    url = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, nullable=False)


class Collection(Base):
    __tablename__ = "collections"

    user_id = Column(ForeignKey('users.user_id'), primary_key=True)
    gif_id = Column(ForeignKey('gifs.gif_id'), primary_key=True)

    date_of_get = Column(DateTime, nullable=False)

    gif = relationship("Gif")