from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    isActive = Column(Boolean, default=True)
    text = 0
    anouncement = 0

    def __repr__(self):
        return self.title


engine = create_engine('sqlite:///shop.db')
Base.metadata.create_all(engine)
