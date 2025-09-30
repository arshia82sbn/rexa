import logging

class LogManager:
    """
    Singleton Logger for the application.
    Ensures only one logger instance is created and reused.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:  # Prevent reinitialization
            return
        LogManager._initialized = True

        # Create logger
        self.logger = logging.getLogger("Rexa")
        self.logger.setLevel(logging.DEBUG)

        # Formatter for logs
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - '
            '[%(filename)s:%(lineno)d] - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)

        # Attach handler if not already added
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)

    def get_logger(self):
        """Return the singleton logger instance."""
        return self.logger
def get_logger():
    return LogManager().get_logger()