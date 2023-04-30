from fastapi import FastAPI
from utils.models import *
from session import session
import uvicorn


app = FastAPI()


def get_db():
    SessionLocal = session()
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()


@app.get("/camera")
def get_all_cameras(db):
    cameras = db.query(Camera).all()
    return cameras


@app.get("/product")
def get_all_products(db):
    products = db.query(Product).all()
    return products


@app.get("/shelf")
def get_all_shelves(db):
    shelves = db.query(Shelf).all()
    return shelves


@app.get("/visitor")
def get_all_visitors(db):
    visitors = db.query(Visitor).all()
    return visitors


@app.get("/")
def read_root():
    return {"Show": "db's"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
