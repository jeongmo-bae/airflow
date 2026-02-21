import logging
from typing import Any, Sequence, Mapping

import pendulum

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
def outer(func):
    def wrapper(*args,**kwargs):
        start = pendulum.now(tz='Asia/Seoul')
        logger.debug(f"start : {start}")
        result = func(*args,**kwargs)
        end = pendulum.now(tz='Asia/Seoul')
        logger.debug(f"end : {end}")

        duration = (end - start).total_seconds()
        logger.debug(f"duration : {duration:.6f}s")
        logger.debug(f"duration : {(end - start).microseconds/1000:.3f}ms")
        return result
    return wrapper

@outer
def real_func(owner : str, param1 : str, param2 : str, *args, **kwargs) -> None :
    logger.info(f"owner : {owner}")
    logger.info(f"param1 : {param1}")
    logger.info(f"param2 : {param2}")
    logger.info(f"args : {args}")
    logger.info(f"kwargs : {kwargs}")
    return None

real_func_with_decorator = real_func(
    "jungmo",
    "p1",
    "p2",
    "arg1",
    2,
    ["arg3"],
    True,
    **{"kwarg1" : 100,"kwarg2":"kw2"},
    kwarg3=True,
    kwarg4=False,
)