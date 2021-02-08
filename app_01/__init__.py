from fastapi import FastAPI
from loguru import logger

from app_01.exception import init_exception
from app_01.router.image import router
from app_01.router.link2pdf import router_l2p

_version_ = '1.0b'


def start_app():
    app = FastAPI(
        title='Comensando con base_64',
        description='Manera simple para aprender a organizar do projecto ',
        version=_version_
    )
    # add exceptions
    app = init_exception(app)
    # Add routing.
    app.include_router(router, tags=['Images Tratamient'])
    app.include_router(router_l2p, tags=['From link obtain HTML code'])

    # Poner el logger a la app
    logger.info('[0] APPLICATION CREATED, READY TO UP.')

    # Return app
    return app
