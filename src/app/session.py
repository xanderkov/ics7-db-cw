import sqlalchemy
from sqlalchemy import create_engine, select, insert, update, delete, func
from sqlalchemy.orm import Session, sessionmaker, class_mapper
from utils.models import *


def create_session(recreate=False):
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        f'postgresql://postgres:postgres@localhost:6432/shop',
        pool_pre_ping=True)
    try:
        engine.connect()
        print("БД  успешно подключена!")
    except:
        print("Ошибка соединения c БД!")
        return

    Session = sessionmaker(bind=engine)
    db = Session()

    if recreate:
        BASE.metadata.create_all(engine)

    return db


def get_db():
    db = create_session()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    create_session(True)

