import base64
import binascii
import traceback

from app_01.exception.exc import RequestException


def is_base_64(base_64: str):
    try:
        base64.b64decode(base_64)
    except binascii.Error:
        raise RequestException(stacktrace=traceback.format_exc())



