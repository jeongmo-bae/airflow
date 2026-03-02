import time
import logging
from functools import wraps
from .logger import MyLogger

logger = MyLogger(__name__)

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            end = time.perf_counter()
            logger.info(f"++++++++++ {func.__name__} took {end - start:.6f} seconds ++++++++++")
            return result
        except Exception as e:
            logger.error(f"---------- {func.__name__} failed after {time.perf_counter() - start:.6f}s : {e} ----------")
            raise
    return wrapper