
from loguru import logger


class APiException(Exception):
    def __init__(self, stacktrace: str, code: int = 404, message: str = "OPERATION ERROR"):
        self.code = code
        self.message = message
        self.stacktrace = stacktrace
        logger.info(f'[-] {message}, STATUS: {code}')


class RequestException(APiException):
    def __init__(self, stacktrace):
        message = 'WRONG BASE64 FORMAT'
        super().__init__(stacktrace, 401, message)
