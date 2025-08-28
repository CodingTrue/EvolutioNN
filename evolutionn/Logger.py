import logging
from colorama import init, Fore

init()

LOG_LEVEL_COLORS = {
    logging.DEBUG: Fore.LIGHTCYAN_EX,
    logging.INFO: Fore.LIGHTGREEN_EX,
    logging.WARN: Fore.LIGHTYELLOW_EX,
    logging.ERROR: Fore.LIGHTRED_EX
}

TEXT_LOG_LEVEL_COLORS = {
    logging.DEBUG: Fore.CYAN,
    logging.INFO: Fore.GREEN,
    logging.WARN: Fore.YELLOW,
    logging.ERROR: Fore.RED
}

def make_message(args: list) -> str:
    return f"\n{'':<12}".join(str(arg) for arg in args)

class LoggerFormatter(logging.Formatter):
    def format(self, record):
        levelno = record.levelno
        level_color, text_color = LOG_LEVEL_COLORS.get(levelno) or Fore.WHITE, TEXT_LOG_LEVEL_COLORS.get(levelno) or Fore.WHITE

        return f"{level_color}{record.levelname:<12}{text_color}{record.getMessage()}"

class Logger:
    def __init__(self):
        self.logger = logging.Logger("main")
        console_handler = logging.StreamHandler()

        console_handler.setFormatter(fmt=LoggerFormatter())

        console_handler.setLevel(level=logging.DEBUG)
        self.logger.setLevel(level=logging.DEBUG)

        self.logger.addHandler(console_handler)

    def debug(self, *args, **kwargs):
        self.logger.debug(make_message(args), **kwargs)

    def info(self, *args, **kwargs):
        self.logger.info(make_message(args), **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(make_message(args), **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(make_message(args), **kwargs)

logger = Logger()