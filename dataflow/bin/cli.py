import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    logger.info("We are just testing")


def parse_cmd_args() -> list:
    logger.info('Okay it works')
