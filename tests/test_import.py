""" C
"""

from lgg import get_logger
from lgg import logger


def test_import():
    """ C
    """
    get_logger()


def test_logging():
    """ C
    """

    logger.info('This is an info message')
    logger.debug('Debugging message')
    logger.error('Error message')
    logger.warning('File not found! An empty one is created')
