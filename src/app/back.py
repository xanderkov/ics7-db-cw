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
    return {"status": "success", "visitor": new_visitor}


@app.post("/camera", status_code=status.HTTP_201_CREATED)
def create_camera(payload: CameraSchema, db: Session = Depends(get_db)):
    new_camera = Camera(**payload.dict())
    db.add(new_camera)
    db.commit()
    db.refresh(new_camera)
    return {"status": "success", "camera": new_camera}


@app.post("/product", status_code=status.HTTP_201_CREATED)
def create_visitor(payload: ProductSchema, db: Session = Depends(get_db)):
    new_product = Product(**payload.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"status": "success", "product": new_product}


@app.post("/shelf", status_code=status.HTTP_201_CREATED)
def create_visitor(payload: ShelfSchema, db: Session = Depends(get_db)):
    new_shelf = Shelf(**payload.dict())
    db.add(new_shelf)
    db.commit()
    db.refresh(new_shelf)
    return {"status": "success", "shelf": new_shelf}


# Update

@app.patch('/visitor/{visitorId}')
def update_visitor(visitorId: str, payload: VisitorSchema, db: Session = Depends(get_db)):
    visitor_query = db.query(Visitor).filter(Visitor.id == visitorId)
    db_visitor = visitor_query.first()
    if not db_visitor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No visitor with this id: {visitorId} found')
    update_data = payload.dict(exclude_unset=True)
    visitor_query.filter(Visitor.id == visitorId).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_visitor)
    return {"status": "success", "visitor": db_visitor}


@app.patch('/camera/{cameraId}')
def update_camera(cameraId: str, payload: CameraSchema, db: Session = Depends(get_db)):
    camera_query = db.query(Camera).filter(Camera.id == cameraId)
    db_camera = camera_query.first()
    if not db_camera:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No camera with this id: {cameraId} found')
    update_data = payload.dict(exclude_unset=True)
    camera_query.filter(Camera.id == cameraId).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_camera)
    return {"status": "success", "camera": db_camera}


@app.patch('/product/{productId}')
def update_product(productId: str, payload: ProductSchema, db: Session = Depends(get_db)):
    product_query = db.query(product).filter(Product.id == productId)
    db_product = product_query.first()
    if not db_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No product with this id: {productId} found')
    update_data = payload.dict(exclude_unset=True)
    product_query.filter(Product.id == productId).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_product)
    return {"status": "success", "product": db_product}


@app.patch('/shelf/{shelfId}')
def update_shelf(shelfId: str, payload: CameraSchema, db: Session = Depends(get_db)):
    shelf_query = db.query(Shelf).filter(Shelf.id == shelfId)
    db_shelf = shelf_query.first()
    if not db_shelf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No shelf with this id: {shelfId} found')
    update_data = payload.dict(exclude_unset=True)
    shelf_query.filter(Shelf.id == shelfId).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_shelf)
    return {"status": "success", "shelf": db_shelf}


# Delete

@app.delete('/visitor/delete/{visitorId}')
def delete_visitor(visitorId: str, db: Session = Depends(get_db)):
    visitor_query = db.query(Visitor).filter(Visitor.id == visitorId)
    visitor = visitor_query.first()
    if not visitor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No visitor with this id: {id} found')
    visitor_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete('/camera/delete/{cameraId}')
def delete_camera(cameraId: str, db: Session = Depends(get_db)):
    camera_query = db.query(Camera).filter(Camera.id == cameraId)
    camera = camera_query.first()
    if not camera:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No camera with this id: {id} found')
    camera_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete('/shelf/delete/{shelfId}')
def delete_shelf(shelfId: str, db: Session = Depends(get_db)):
    shelf_query = db.query(Shelf).filter(Shelf.id == shelfId)
    shelf = shelf_query.first()
    if not shelf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No shelf with this id: {id} found')
    shelf_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.delete('/product/delete/{productId}')
def delete_product(productId: str, db: Session = Depends(get_db)):
    product_query = db.query(Product).filter(Product.id == productId)
    product = product_query.first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No product with this id: {id} found')
    product_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
