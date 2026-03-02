import os.path

import pendulum
from dateutil import relativedelta
from python.common.logger import MyLogger

logger = MyLogger(os.path.basename(__file__)) # __name__

now = pendulum.now(tz='Asia/Seoul')

logger.info(f'pendulum.datetime : {type(now)}')
logger.debug(now)
logger.warning(f'now + relativedelta.relativedelta(days=-1) : {now + relativedelta.relativedelta(days=-1)}')

logger.info(f'pendulum.now.weekday : {pendulum.now(tz='Asia/Seoul').weekday()}')