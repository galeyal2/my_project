import logging


class SingletonLoggerMeta(type):
    _instances = {}

    def __call__(cls, name, *args, **kwargs):
        if name not in cls._instances:
            cls._instances[name] = super().__call__(name, *args, **kwargs)
        return cls._instances[name]


class MyLogger(metaclass=SingletonLoggerMeta):

    def __init__(self, name: str, logger_mode: str = 'INFO'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logger_mode)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)


name = "eyal"
eyal: MyLogger = MyLogger(name, "INFO")
eyal_logger = eyal.logger
eyal_logger.info(f"logger has started as {name}")
