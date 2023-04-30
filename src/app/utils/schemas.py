from pydantic import BaseModel
from datetime import datetime


class VisitorSchema(BaseModel):
    id: int | None = None
    description: str | None = None
    location: str | None = None
    view: str | None = None
    detection: str | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class CameraSchema(BaseModel):
    id: int | None = None
    location: str | None = None
    resolution: str | None = None
    rotation: str | None = None
    cam_type: str | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class CameraVisitorSchema(BaseModel):
    id_vis: int | None = None
    id_cam: int | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ShelfSchema(BaseModel):
    id: int | None = None
    location: str | None = None
    length: float | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ShelfVisitorSchema(BaseModel):
    id_shelf: int | None = None
    id_cam: int | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ProductSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    location: str | None = None
    dataEnd: datetime | None = None
    weight: float | None = None
    status: int | None = None
    price: int | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ShelfProductSchema(BaseModel):
    id_shelf: int | None = None
    id_product: int | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ChainStoreSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    location: str | None = None
    nameDir: str | None = None
    income: float | None = None
    consumption: float | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
