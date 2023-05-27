from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shop

engine = create_engine('sqlite:///shop.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)

session = DBsession()

# CREATE
shopOne = Shop(title=" ", members=" ", discography=" ")
session.add(shopOne)
session.commit()

# READ
all_shops = session.query(Shop).all()
first_shop = session.query(Shop).first()

# UPDATE
editedShop = session.quary(Shop).filter_by(id=1).one()
editedShop.title = " "
session.add(editedShop)
session.commit()

# DELETE
shopToDelete = session.query(Shop).filter_by(title=' ').one()
session.delete(shopToDelete)
session.commit()

session.rollback()
