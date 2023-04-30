import sqlalchemy
from sqlalchemy import create_engine, select, insert, update, delete, func
from sqlalchemy.orm import Session, sessionmaker, class_mapper
from utils.models import *

def main():
    print("Версия SQL Alchemy:", sqlalchemy.__version__)

    engine = create_engine(
        f'postgresql://postgres:postgres@localhost:6432/shop',
        pool_pre_ping=True)
    try:
        engine.connect()
        print("БД  успешно подключена!")
    except:
        print("Ошибка соединения к БД!")
        return

    Session = sessionmaker(bind=engine)
    session = Session()
    BASE.metadata.create_all(engine)


if __name__ == "__main__":
    main()