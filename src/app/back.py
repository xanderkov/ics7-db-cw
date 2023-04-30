from fastapi import FastAPI, Depends, HTTPException, status, APIRouter, Response

from utils.models import *
from utils.schemas import *
from session import create_session, get_db
import uvicorn
from sqlalchemy.orm import Session


app = FastAPI()

# Read


@app.get("/camera")
def get_all_cameras(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    cameras = db.query(Camera).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(cameras), 'cameras': cameras}


@app.get("/product")
def get_all_products(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    products = db.query(Product).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(products), 'products': products}


@app.get("/shelf")
def get_all_shelves(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    shelfs = db.query(Shelf).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(shelfs), 'shelfs': shelfs}


@app.get("/visitor")
def get_all_visitors(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
    skip = (page - 1) * limit
    visitors = db.query(Visitor).limit(limit).offset(skip).all()
    return {'status': 'success', 'results': len(visitors), 'visitors': visitors}


# Create

@app.post("/visitor", status_code=status.HTTP_201_CREATED)
def create_visitor(payload: VisitorSchema, db: Session = Depends(get_db)):
    new_visitor = Visitor(**payload.dict())
    db.add(new_visitor)
    db.commit()
    db.refresh(new_visitor)
    return {"status": "success", "note": new_visitor}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
