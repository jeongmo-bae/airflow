import logging

class MyLogger :
    _initialized = False
    def __init__(self,name):
        if not self._initialized:
            logging.basicConfig(
                level=logging.DEBUG,
                format='%(asctime)s [%(levelname)-7s] %(name)s:line %(lineno)d >>> %(message)s',
            )
            self._initialized = True
        self.logger = logging.getLogger(name)

    def debug(self, msg):
        self.logger.debug(msg,stacklevel=2)

    def info(self, msg):
        self.logger.info(msg,stacklevel=2)

    def warning(self, msg):
        self.logger.warning(msg,stacklevel=2)

    def error(self, msg):
        self.logger.error(msg,stacklevel=2)
