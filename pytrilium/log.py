import logging
import sys
import coloredlogs
from logging.handlers import TimedRotatingFileHandler

FMT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FMT = "%m-%d-%Y %H:%M"

FILE_FORMATTER = logging.Formatter("%(asctime)s - %(funcName)s:%(lineno)d - %(name)s - %(levelname)s - %(message)s")
CONSOLE_FORMATTER = logging.Formatter(FMT)

# humanfriendly --demo
CUSTOM_FIELD_STYLES = {
    "asctime": {"color": "green"},
    "hostname": {"color": "magenta"},
    "levelname": {"bold": True, "color": "black"},
    "name": {"color": 200},
    "programname": {"color": "cyan"},
    "username": {"color": "yellow"},
}


def get_console_handler(debug):
    """
    Since we don't want to overwhelm or freak out the user, we're just going to send the output
    of debugging over to the file, and only send INFO out to the user.
    """

    # First, let's set the console StreamHandler
    console_handler = logging.StreamHandler(sys.stdout)

    # If debug is true, print it out to the screen.
    if debug == True:
        console_handler.setLevel(logging.DEBUG)
    else:
        console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(CONSOLE_FORMATTER)
    return console_handler


def get_file_handler(debug=False, log_file_name="log.txt"):
    """
    We're going to print out the debug output to the log file.
    """

    file_handler = TimedRotatingFileHandler(log_file_name, when="midnight")

    # We want to print out debug information to this file.
    if debug:
        file_handler.setLevel(logging.DEBUG)
    else:
        file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(FILE_FORMATTER)
    return file_handler


def get_logger(
    logger_name="Template Repository Logger",
    log_file_name="log.txt",
    debug=False,
    create_log_file=True,
):
    """Get the logger, for the current namespace.

    Args:
        logger_name (str, optional): Logger Name. Defaults to "Template Repository Logger".
        debug (bool, optional): Debugger boolean. Defaults to False.

    Returns:
        logger: return the logger for the current namespace, if it exists. If it does not, create it.
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # If the logger already has the two handlers we've set, no need to add more.
    if len(logger.handlers) < 2:
        logger.addHandler(get_console_handler(debug))
        if create_log_file != False:
            logger.addHandler(get_file_handler(debug, log_file_name=log_file_name))
        # If debugging is not true, we don't want to output DEBUG information to the console.
        if debug != False:
            coloredlogs.install(
                level="DEBUG",
                logger=logger,
                datefmt=DATE_FMT,
                fmt=FMT,
                field_styles=CUSTOM_FIELD_STYLES,
            )
            logger.debug("Added the debug logger to the console output...")
        else:
            coloredlogs.install(
                level="INFO",
                logger=logger,
                datefmt=DATE_FMT,
                fmt=FMT,
                field_styles=CUSTOM_FIELD_STYLES,
            )

    # With this pattern, it's rarely necessary to propagate the error up to parent.
    logger.propagate = False
    logger.debug("Returning logger to process...")

    return logger
