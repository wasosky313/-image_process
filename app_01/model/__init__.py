from pydantic import BaseModel


class Item(BaseModel):
    base_64: str


class Retorno(BaseModel):
    width: str
    height: str


class GrayOut(BaseModel):
    gray_out: str


class RotateIn(BaseModel):
    base_64: str
    angle: int


class RotateOut(BaseModel):
    rotate_out: str


class ResizeIn(BaseModel):
    base_64: str
    width: int
    height: int


class ResizeOut(BaseModel):
    resize_out: str


class LinkIn(BaseModel):
    url: str


class LinkOut(BaseModel):
    link: str
    html: str
