""" C
"""

from lgg import get_logger
from lgg import logger


def test_anonymous():
    """ C
    """
    assert logger.name == 'nameless'


def test_different_names():
    """ C
    """
    print()
    list_range = list(range(1, 4))
    loggers = [get_logger(f'logger{i}') for i in list_range]

    for i, _logger in zip(list_range, loggers):
        assert _logger.name == f'logger{i}'
        _logger.info(f'Hello from logger {i}')


def test_same_names():
    """ C
    """
    loggers = [get_logger('logger_name') for _ in range(2)]

    for _logger in loggers:
        _logger.info('Hello!')
        _logger.error('Bye!')
