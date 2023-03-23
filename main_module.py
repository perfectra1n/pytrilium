import argparse
import traceback

# Local import
import log
from cli_color import Color

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="This is the description for the main parser!"
        )
        parser.add_argument(
            "required_arg",
            help="Required. This is the description for the main requirement.",
        )
        parser.add_argument(
            "--debug",
            action="store_true",
            help="Optional. Use this argument if you are debugging any errors.",
        )

        args = parser.parse_args()

        logger = log.get_logger(
            logger_name=__file__ + " Logger",
            log_file_name=__file__ + ".log",
            debug=args.debug,
        )

        logger.debug("This is the debug logger!")
        logger.info(Color.white(f"This is {__file__}"))

    except Exception:
        logger.error("Unhandled Exception!")
        logger.error(traceback.format_exc())
