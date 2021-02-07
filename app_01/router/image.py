from fastapi import APIRouter
import base64
import io
from PIL import Image, ImageOps

from app_01.model import Item, Retorno, GrayOut, RotateOut, ResizeOut, RotateIn, ResizeIn
from app_01.util import is_base_64

router = APIRouter()


@router.post("/anchors/")
async def anchors(item: Item):
    is_base_64(item.base_64)

    imgdata = base64.b64decode(item.base_64)
    im = Image.open(io.BytesIO(imgdata))
    width, height = im.size

    return Retorno(width=width, height=height)


# grayscale not yet
@router.post("/gray/")
async def img_grayscale(item: Item):
    is_base_64(item.base_64)

    buffer = io.BytesIO()
    imgdata = base64.b64decode(item.base_64)
    img = Image.open(io.BytesIO(imgdata))
    new_img = ImageOps.grayscale(img)
    new_img.save(buffer, format="PNG")

    gray_image_64 = base64.b64encode(buffer.getvalue())

    return GrayOut(gray_out=gray_image_64)


# rotate
@router.post("/rotate/")
async def img_rotate(item: RotateIn):
    is_base_64(item.base_64)

    buffer = io.BytesIO()
    imgdata = base64.b64decode(item.base_64)
    img = Image.open(io.BytesIO(imgdata))
    new_img = img.rotate(item.angle)
    new_img.save(buffer, format="PNG")

    im_base_64 = base64.b64encode(buffer.getvalue())

    return RotateOut(rotate_out=im_base_64)


# resize image
@router.post("/resize/")
async def img_resize(item: ResizeIn):
    is_base_64(item.base_64)

    buffer = io.BytesIO()
    imgdata = base64.b64decode(item.base_64)
    img = Image.open(io.BytesIO(imgdata))
    new_img = img.resize((item.width, item.height))
    new_img.save(buffer, format="PNG")
    img_b64 = base64.b64encode(buffer.getvalue())

    return ResizeOut(resize_out=str(img_b64)[2:-1])
